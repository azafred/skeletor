#!/bin/bash
if [ $# -eq 0 ]
then
    echo "You must specify the name of the project as an argument!"
    exit 1
fi

# Replacing every occurence of Sample with the project name.
for f in `rg myproj -l`; do 
    sed -i.bak "s/myproj/$1/" $f
    find ./ -name '*.bak' -delete
done

