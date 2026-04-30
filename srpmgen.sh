#!/bin/bash

set -xe

bd=$(dirname $(readlink -f $0))

# Allow dist tag to be overridden via environment
DIST_TAG="${DIST_TAG:-fc45}"
WORK_DIR="${WORK_DIR:-$HOME/work/last}"

# Ensure output directory exists
test -d "$WORK_DIR" || {
    echo "ERROR: Output directory $WORK_DIR doesn't exist"
    exit 1
}

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

# Build SRPM
pushd "$bd/rpmbuild/SPECS"
rpmbuild --define "_topdir $bd/rpmbuild" --define "dist .$DIST_TAG" -bs cow.spec
popd

# Copy to output location
cp "$bd/rpmbuild/SRPMS/cow"*.src.rpm "$WORK_DIR/"
