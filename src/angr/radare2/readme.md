# Radare2

## Source

- [radare2 tutorial by Megabeets](https://www.megabeets.net/a-journey-into-radare-2-part-1/)
- [radare2](https://www.radare.org/r/down.html)
- [x86 Assembly Guide](http://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html)

## What comes with radare2

Get information from the binary
```bash
rabin2 -I megabeets_0x1
```

Get into radare2
```bash
r2 ./megabeets_0x1
r2 -A megabeets_0x1 # to analyse the binary while going to radare2 
```

Rot13 cipher
```bash
rahash2 -E rot -S s:13 -s ‘Megabeets\n‘
```

## Inside Radare2

You should know you are inside radare2 if you see something like:
```bash
$ r2 ./megabeets_0x1_mac
 -- Using radare2 to generate intelligence ...
[0x100000e80]>
```

Use [q] to quit.

Get the entry point
```bash
ie  # i for info, e for entrypoint
```

Analyse the binary
```bash
a?  # a for analysis, ? to get the help
```

After the analysis radare2 associates names to interesting offsets in the file such as Sections, Function, Symbols, Strings, etc.
Those names are called ‘flags’. Flags can be grouped into ‘flag spaces’. 
A flag space is a namespace for flags of similar characteristics or type.
```bash
fs  # f for flag, s for space
fs imports; f  # select the flags in imports, and print it 
fs strings; f  # select the flags in strings, and print it 
```

Looking for strings inside the binary:
```bash
iz   # list strings in data sections
izz  # list strings in the whole binary
axt @@ str.*  # See where the strings are used within the program
```

Looking for functions inside of the binary:
```bash
afl  # a for analysis, f for fonction, l for list
```

Looking at some binary:
```bash
s main        # s for seek, main the symbolic name of the program, seek the bit
pdf           # p for print, d for disassemble, f for function, to look at the assembly code
pd $r @ main  # p for print, d for disassemble the main
VV @ main    # Visual view of the program in main
```

Disassembling:
```bash
# @@ is an iterator
# @ is used as a temporary seeking. i.e “print the function at offset sym.beet”.
pdf @ sym._beet
? 0x88  # To get info on the value
```

Reopen in debug mode with an argument:
```bash
ood Zrtnorrgf
dc  # to continue executing the binary
```
