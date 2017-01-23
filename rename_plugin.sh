#!/usr/bin/env bash


caps="DATA_DMS"
underscore="_data_dms"
hyphen="-data-dms"
camelL="dataDms"
camelU="DataDms"

set nounset
set errexit

function replace {
    from=$1
    to=$2

    for d in `find ./ -type d -not -name '.git'`
    do
        new=`echo $d | sed "s/$from/$to/g"`
        [ "$d" != "$new" ] && mv $d $new
    done

    for f in `find ./ -type f -not -name '.git'`
    do
        new=`echo $f | sed "s/$from/$to/g"`
        [ "$f" != "$new" ] && mv $f $new
    done

    for f in `find ./ -type f -not -name '.git'`
    do
        sed -i "s/$from/$to/g" $f
    done

}

replace "_data_dms"  "$underscore"
replace "-data-dms" "$hyphen"
replace "DATA_DMS" "$caps"
replace "DataDms" "$camelU"
# replace "DataDms" "$camelL"

# Remove compile generated javascript
find ./ -type f -not -name '.git' -name "*.js" -exec rm {} \; || true
find ./ -type f -not -name '.git' -name "*.js.map" -exec rm {} \; || true

# remove the git index
[ -f .git/index ] && rm .git/index || true
