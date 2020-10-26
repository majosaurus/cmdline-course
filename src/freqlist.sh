#! /bin/bash

cat $1 |
tr '[:upper:]' '[:lower:]' |
tr -s '[:space:]' '\n' |
tr -d '[:punct:]' |
sort | 
uniq -c | 
sort -nr > $2
