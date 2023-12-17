#!/bin/bash

# ver. Sun/17/Dec/2023
#
# Made by: CyberCoral
# ------------------------------------------------
# Github:
# https://www.github.com/CyberCoral
#

loop=$1
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

right_s=1
text_files=("${@:2:$#}")
text_file=("'${text_files[0]}'")

len=${#text_files[@]}

for (( i=1;$i<$len ;i++ )); do
    text_file="${text_file[@]},'${text_files[i]}'"
done

echo "import VLC_auto_player">>VLC.py
echo "from VLC_auto_player import VLC_auto_player as VLC">>VLC.py
echo "VLC($loop,False,txt_files=[${text_file[@]}],right_s=$right_s)">>VLC.py
python -m VLC
rm VLC.py
