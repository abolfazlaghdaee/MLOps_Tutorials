#!/bin/bash


counter=1


while IFS= read -r line; do

    echo "$counter: $line"




    counter=$((counter + 1))

done < /etc/passwd
