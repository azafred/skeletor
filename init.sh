#!/bin/bash
echo "Running init...."

if [ $# -eq 0 ]
then
    echo "You must specify the name of the project as an argument!"
    exit 1
fi

# Replacing every occurence of Sample with the project name.
echo "Finding all the occurences of 'sample' and replacing them with $1..."
for f in `rg sample -l`; do 
    sed -i.bak "s/sample/$1/" $f
    find ./ -name '*.bak' -delete
done

touch initialized
