#!/bin/bash

# ver. Sat/16/Dec/2023
#
# Made by: CyberCoral
# ------------------------------------------------
# Github:
# https://www.github.com/CyberCoral
#

file=$1
links=("${@:1:$#}")
for ((i=1;i<=$#;i++)); do
    echo "${links[i]}">>$file
done