#!/bin/bash

set -o nounset
set -o errexit
set -x

PAPP_NAME='papp_noop'

function convertBambooDate() {
# EG s="2010-01-01T01:00:00.000+01:00"
# TO 100101.0100
python <<EOF
from dateutil.parser import parse
print parse("${BAMBOO_DATE}").strftime('%y%m%d.%H%M')
EOF
}
echo "start version is $VER"

BUILD="${BUILD}"
VER="${VER}"
DATE="`convertBambooDate`"

if [ "${VER}" == '${bamboo.jira.version}' ]; then
    VER="b${DATE}"
fi

echo "New version is $VER"
echo "New build is $BUILD"

TAR_DIR="${PAPP_NAME}_$VER#$BUILD"
DIR="deploy/$TAR_DIR"
mkdir -p $DIR/cpython

echo "New version is $VER"


# Source
cp -pr ${PAPP_NAME}/alembic $DIR/cpython
cp -pr ${PAPP_NAME}/src/${PAPP_NAME} $DIR/cpython
cp -pr ${PAPP_NAME}/papp_changelog.json $DIR
cp -pr ${PAPP_NAME}/papp_version.json $DIR


find $DIR -iname .git -exec rm -rf {} \; || true
find $DIR -iname "test" -exec rm -rf {} \; 2> /dev/null || true
find $DIR -iname "tests" -exec rm -rf {} \; 2> /dev/null || true
find $DIR -iname "*test.py" -exec rm -rf {} \; || true
find $DIR -iname "*tests.py" -exec rm -rf {} \; || true
find $DIR -iname ".Apple*" -exec rm -rf {} \; || true
find $DIR -iname "*TODO*" -exec rm -rf {} \; || true
find $DIR -iname ".idea" -exec rm -rf {} \; || true


# Apply version number

for f in `grep -l -r  '#PAPP_VER#' .`; do
    echo "Updating version in file $f"
    sed -i "s/#PAPP_VER#/$VER/g" $f
done

for f in `grep -l -r  '#PAPP_BUILD#' .`; do
    echo "Updating build in file $f"
    sed -i "s/#PAPP_BUILD#/$BUILD/g" $f
done

for f in `grep -l -r  '#BUILD_DATE#' .`; do
    echo "Updating date in file $f"
    sed -i "s/#BUILD_DATE#/$DATE/g" $f
done

cp -pr $DIR/cpython $DIR/pypy

echo "Compiling all python modules"
( cd $DIR/cpython && python -m compileall -f . )

# PYPY doesn't accept compiled files with out source

#echo "Compiling all pypy modules"
#( cd $DIR/pypy && pypy -m compileall -b -f . )

echo "Deleting just cpython source files"
find $DIR/cpython -name "*.py" -exec rm {} \;


tar cjf ${TAR_DIR}.tar.bz2 -C deploy $TAR_DIR
