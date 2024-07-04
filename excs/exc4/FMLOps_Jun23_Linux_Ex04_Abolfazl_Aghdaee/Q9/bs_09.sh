#!/bin/bash


date=$(date +%Y%m%d)

shopt -s nullglob


for file in *.jpg; do


    filename="${file%.*}"


    mv "$file" "${date}${filename}.jpg"
done


shopt -u nullglob

echo "Renaming completed."
