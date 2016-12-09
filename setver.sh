#!/usr/bin/env bash

set -o nounset
set -o errexit
#set -x

if ! [ -f "setup.py" ]; then
    echo "setver.sh must be run in the directory where setup.py is"
    exit 1
fi


VER="${1:?You must pass a version of the format 0.0.0 as the only argument}"

echo "Setting version to $VER"

DOWNLOAD_URL="    download_url='"
DOWNLOAD_URL="${DOWNLOAD_URL}https://github.com/Synerty/papp_noop/tarball/${VER}',"

VERSION="    version='"
VERSION="${VERSION}${VER}',"

sed -i "s;.* download_url=.*;${DOWNLOAD_URL};"  setup.py
sed -i "s;.* version=.*;${VERSION};"  setup.py

