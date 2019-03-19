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


### References

Whenever you see something `0x45` it's an hexadecimal representation of a byte.

Register in memory:

| 8-byte register | Bytes 0-3 | Bytes 0-1 | Byte 0 |
|-----------------|-----------|-----------|--------|
| rax             | eax       | ax        | al     |

> When there's a `r` it is a register so 8 bytes, when it is a `e` it is bytes 0 to 3.

Commands in assembly:

- `lea <destination> <source>` : load source adress into destination
- `mov <destination> <source>` : Move source address into destination
- `cmp <value1> <value2>` : Compare source value1 with value2
- `je <address>` : Jump to the specified address if the above comparison is equal
- `add <destination> <value>` : Add the value at the destination address value.

Common assembly registers:

- rax - register a extended (for data)
- rdi - register destination index (destination for data copies)

## Analysis

That the time where we look at the disassembled main to understand what is happening.
Radare2 is very good at deciphering through the assembly instructions, 
you can have a look into `serial_disassembled.txt`.

We can deduce that the variable s `rbp-0x200` is the entered input here. 
Shortly after that we can see that its length is checked `strlen`, the serial number should be 16 `0x10`.


```assembly
|           0x00400a19      488d8500feff.  lea rax, [s]                ; load rax with the value of s
|           0x00400a20      4889c7         mov rdi, rax                ; const char *s
|           0x00400a23      e828feffff     call sym.imp.strlen         ; size_t strlen(const char *s)
|           0x00400a28      4883f810       cmp rax, 0x10               ; compare with 16
|       ,=< 0x00400a2c      740e           je 0x400a3c                 ; jump when equal to 0x400a3c 
```


Then we can see that the first byte `al` of the input is compared with E (1 ASCII character is 8bits -> 1 byte).

```assembly
|       `-> 0x00400a3c      0fb68500feff.  movzx eax, byte [s]         ; Move the 4 bytes in memory in [s] into EAX
|           0x00400a43      3c45           cmp al, 0x45                ; compare the first byte with 'E' ; 69
|       ,=< 0x00400a45      740e           je 0x400a55                 ; jump when equal to 0x400a55
```

Then a hard coded value `[var_1f1h]` is added and the result is compared with the input. 
So we can skip and try to find all of the easy constraints we can find.

```assembly
|       `-> 0x00400a55      0fb68500feff.  movzx eax, byte [s]         ; Same as before
|           0x00400a5c      0fbed0         movsx edx, al               ; Move al to edx 
|           0x00400a5f      0fb6850ffeff.  movzx eax, byte [var_1f1h]  ; Move variable [var_1f1h] to eax
|           0x00400a66      0fbec0         movsx eax, al               ; Move al to eax
|           0x00400a69      01d0           add eax, edx                ; Add edx to eax
|           0x00400a6b      3d9b000000     cmp eax, 0x9b               ; compare eax with 155
|           0x00400a70      740e           je 0x400a80
```