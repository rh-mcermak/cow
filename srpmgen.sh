#!/bin/bash

set -xe

bd=$(dirname $(readlink -f $0))

rm -rf $bd/rpmbuild
mkdir -p $bd/rpmbuild/{SPECS,SOURCES}

rm -rf $bd/src
git clone https://codeberg.org/thomasadam/cow.git src
pushd src
git archive --format=tar.gz --prefix=cow-1.0/ -o ../rpmbuild/SOURCES/cow-1.0.tar.gz HEAD
# Short git hash
h=$(git rev-parse --short HEAD)
popd

# Kind of timestamp ensuring clean upgrade path
s=$(($(date +%s) - 1770000000))

cat $bd/cow.spec | sed "s/STAMP/$s/" | sed "s/HASH/$h/" >  $bd/rpmbuild/SPECS/cow.spec

pushd rpmbuild/SPECS
rpmbuild --define "_topdir $bd/rpmbuild" --define "dist .fc45" -bs cow.spec
popd

cp $bd/rpmbuild/SRPMS/cow*.src.rpm ~/work/last
