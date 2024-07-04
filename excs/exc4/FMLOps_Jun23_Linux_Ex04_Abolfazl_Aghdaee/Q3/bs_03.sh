#!/bin/bash


read -p "Enter the name of a file or directory: " file 


if [ -e "$file" ]
   then



    if [ -f "$file" ]
       then
        echo "$file is a regular file."


    elif [ -d "$file" ]
        then
        echo "$file is a directory."

    else
        echo "$file is another type of file."
    fi


    ls -l "$file"
else
    echo "$file does not exist."
fi
