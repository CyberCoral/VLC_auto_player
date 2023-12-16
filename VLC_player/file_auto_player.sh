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

files=("${@:2:$#}")
file=("'${files[0]}'")

len=${#files[@]}

for (( i=1;$i<$len ;i++ )); do
    file="${file[@]},'${files[i]}'"
done

echo "import VLC_auto_player">>reproduce_file_VLC.py
echo "from VLC_auto_player import file_auto_player as VLC">>reproduce_file_VLC.py
echo "VLC($loop,False,files=[${file[@]}])">>reproduce_file_VLC.py
python -m reproduce_file_VLC
rm reproduce_file_VLC.py