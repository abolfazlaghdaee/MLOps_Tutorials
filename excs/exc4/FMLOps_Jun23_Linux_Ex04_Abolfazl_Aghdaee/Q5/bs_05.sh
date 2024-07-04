#!/bin/bash


if [ $# -eq 0 ]
 then
    echo "Usage: $0 <file>"
    exit 1
fi


for file in "$@"
 do

    if [ -e "$file" ]
 then
        
        if [ -f "$file" ]
 then

            echo "$file is a regular file."


        elif [ -d "$file" ]; then
            echo "$file is a directory."


        else
            echo "$file is another type of file."
        fi


        ls -l "$file"
    else
        echo "$file does not exist."
    fi
done
