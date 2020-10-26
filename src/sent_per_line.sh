#! /bin/bash

cat $1 |
sed 's/^$/#/' |
tr -s '\n' ' ' | 
sed -E 's/([.?!]) ([A-Z])/\1# \2/g' |
sed -E 's/([IVX][.])# /\1/g' |
tr -s '#' '\n' |
sed 's/^ *//' |
sed 's/ *$//' |
grep -v "^$" > $2