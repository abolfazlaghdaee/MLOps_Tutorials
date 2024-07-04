#!/bin/bash 


file_count(){

num=$(ls -1 | wc -l)

echo "$num"
}


file_count
