#!/bin/bash
for f in `rg myproj -l`; do 
    sed -i.bak "s/myproj/$1/" $f
    find ./ -name '*.bak' -delete
 done
