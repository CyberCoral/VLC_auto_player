#!/bin/bash

# ver. Sun/17/Dec/2023
#
# Made by: CyberCoral
# ------------------------------------------------
# Github:
# https://www.github.com/CyberCoral
#
case "$1" in 
    "true")
    loop="True"
    ;;
    "false")
    loop="False"
    ;;
    *)
    echo "$1 not in [true, false]"
    exit 1
    ;;
esac

case "$2" in 
    "true")
    txt_="True"
    ;;
    "false")
    txt_="False"
    ;;
    *)
    echo "$2 not in [true, false]"
    exit 1
    ;;
esac

files=("${@:3:$#}")
file=("'${files[0]}'")

len=${#files[@]}

for (( i=1;$i<$len ;i++ )); do
    file="${file[@]},'${files[i]}'"
done

echo "import VLC_auto_player">>reproduce_file_VLC.py
echo "from VLC_auto_player import file_auto_player as VLC">>reproduce_file_VLC.py
echo "VLC($loop,False,$txt_,files=[${file[@]}])">>reproduce_file_VLC.py
python -m reproduce_file_VLC
rm reproduce_file_VLC.py
