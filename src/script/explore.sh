#!/bin/bash

file $1
exiftool $1 || echo "exiftool error"
strings -o $1
hexdump -C $1 | head

#png

#pngcheck -vt $1 || echo "error"

#bin

#binwalk -Mre $1
#binwalk -B -E $1
#binwalk -R $1
#binwalk -y 'flag' $1
#binwalk -W --block=8 --length=64 $1
