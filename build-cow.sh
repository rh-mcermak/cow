#!/bin/bash

set -xe

# Check if there's a new upstream update
nhash=$(git ls-remote https://codeberg.org/thomasadam/cow.git HEAD | cut -c1-7)
dnf clean all --disablerepo=\* --enablerepo=\*cow\*
if dnf repoquery '--disablerepo=*' '--enablerepo=*cow*' --quiet --location --srpm --available --latest-limit=15 cow | grep -F "$nhash"; then
   echo "Cow repo is up to date."
   exit 0
fi

bd=$(dirname $(readlink -f $0))

# Allow dist tag to be overridden via environment
DIST_TAG="${DIST_TAG:-fc45}"

# Clean and setup build directories
rm -rf "$bd/rpmbuild"
mkdir -p "$bd/rpmbuild"/{SPECS,SOURCES}

# Clone or update source
if [ -d "$bd/src" ]; then
    echo "Updating existing source..."
    pushd "$bd/src"
    git fetch origin
    git reset --hard origin/main
    popd
else
    echo "Cloning fresh source..."
    git clone https://codeberg.org/thomasadam/cow.git "$bd/src" || {
        echo "ERROR: Failed to clone upstream repository"
        exit 1
    }
fi

pushd "$bd/src"
git archive --format=tar.gz --prefix=cow-1.0/ -o "../rpmbuild/SOURCES/cow-1.0.tar.gz" HEAD
h=$(git rev-parse --short HEAD)
popd

cp "$bd/logging.patch" "$bd/rpmbuild/SOURCES/"

# Timestamp for upgrade path
s=$(($(date +%s) - 1770000000))

# Generate spec with substitutions
sed -i "0,/%changelog/{/%changelog/a\

}" "$bd/cow.spec"
sed -i "0,/%changelog/{/%changelog/a\
- Automated build from upstream git commit $h
}" "$bd/cow.spec"
sed -i "0,/%changelog/{/%changelog/a\
* $(date '+%a %b %d %Y') Martin Cermak <mcermak@redhat.com> - 1-0.$s.$h
}" "$bd/cow.spec"
sed -e "s/STAMP/$s/" -e "s/HASH/$h/" "$bd/cow.spec" > "$bd/rpmbuild/SPECS/cow.spec"

# Edit the spec
vim $bd/rpmbuild/SPECS/cow.spec || exit  # :cq

# Build SRPM
pushd "$bd/rpmbuild/SPECS"
rpmbuild --define "_topdir $bd/rpmbuild" --define "dist .$DIST_TAG" -bs cow.spec
popd

# Build it
# https://copr.fedorainfracloud.org/api/
copr-cli build mcermak/cow  "$bd/rpmbuild/SRPMS/cow"*.src.rpm
