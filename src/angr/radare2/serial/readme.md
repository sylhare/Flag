# Serial

## Introduction

### What's that

Serial is a reverse engineering challenge from SHARIF UNIVERSITY CTF 2016 worth 150 pts.
The goal of this challenge is to find the right serial number which will be the flag I guess.

Like:
```bash
./serial s0m3th!ng
>> Yeah you found the flag!
```

### Reverse engineering

I will be using:
- radare2
- angr
- Other standard tool for reverse engineering

First we are going to explore a bit into this binary.
To do that look into `explore.sh`, unfortunately the `flag` can't be found that easily.
We will need to do some analysis ...


### Sources

I chose this one because it had a lot of write ups including one with angr,
So it would be a good choice to practice with radare2 and angr with a chance of succeeding
while being a total beginner.

- [xil.se](https://github.com/xil-se/xil.se/blob/cbeb4ecc509b0590a7c246096a45e132fe8ce32e/content/post/sharifctf-2016-re6-serial.md)
- [grazfather](http://grazfather.github.io/ctf/re/2016/02/07/Sharif-CTF-RE150-Serial-Writeup.html)
- [0x90r00t](https://0x90r00t.com/2016/02/07/sharif-university-ctf-2016-reverse-150-serial-write-up/)
- [Michael Bann](https://bannsecurity.com/index.php/home/10-ctf-writeups/29-sharif-university-ctf-2016-serial)

## Analysis

That the time where we look at the disassembled main to understand what is happening.
Radare2 is very good at deciphering through the assembly instructions, 
you can have a look into `serial_disassembled.txt`.

