#!/usr/bin/env bash

# Give execution permission and execute (only on linux system)
# chmod +x serial
# ./serial  # Allow to play with it

# Get a look inside
printf "file \n"
file serial

printf "\nstrings \n"
strings -o serial | grep -v '_'

printf "\nbinwalk \n"
binwalk -B serial || echo "binwalk not found"           # Get the file signature
binwalk -R serial || echo "binwalk not found"           # Scan file for a specific sequence of bytes
binwalk -y 'flag' serial   || echo "binwalk not found"  # Look for the word 'Flag inside'


# radare2

printf "\nr2 on serial\n"
# rabin2 -I serial
# r2 ./serial
printf "\naaa
>> Invalid instruction of 1048566 bytes at 0x400ca5y0 (aa)
>> Invalid :instruction of 1048576 bytes at 0x400b9a

iz
>> [Strings]
>> Num Paddr      Vaddr      Len Size Section  Type  String
>> 000 0x00000dac 0x00400dac  28  29 (.rodata) ascii Please Enter the valid key!\n
>> 001 0x00000dc9 0x00400dc9  26  27 (.rodata) ascii Serial number is valid :)\n
>> 002 0x00000de4 0x00400de4  28  29 (.rodata) ascii Serial number is not valid!\n

axt @@ str.*
>> main 0x4009e4 [DATA] mov esi, str.Please_Enter_the_valid_key
>> main 0x400c5c [DATA] mov esi, str.Serial_number_is_valid_:
>> main 0x400c84 [DATA] mov esi, str.Serial_number_is_not_valid

VV
>> Visual view is all messed up

pdf @ main
"
cat serial_disassembled.txt