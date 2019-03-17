# [SHARIF UNIVERSITY CTF 2016](https://0x90r00t.com/2016/02/07/sharif-university-ctf-2016-reverse-150-serial-write-up/) [REVERSE 150 – SERIAL] 

## Description
Run and capture the flag!

```bash
file: serial: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.26, BuildID[sha1]=77e92e8b1bd4f26641bab4dbf563037a7b9538d2, not stripped
```

## Resolution

Same as dMd, the binary is asking for a valid key.
We jump into IDA and can’t find anything really interesting, except some hex data in the code.
We’ll just try to debug it directly, so we put our first breakpoint right after the call which gets our input at 0x400a10. We can see quickly a comparison between our input length and 0x10, so we know the key has to be 16 characters long. Then, the program jumps into memory segment that gdb is not syncronized with, so to help us in the debugging process, we can define a little function for the remaining gdb-session:

```gdb
define hook-stop
Type commands for definition of "hook-stop".
End with a line saying just "end".
>x/2i $rip
>end
```

Everytime we go to the next instruction, we will print the next 2 instructions to be executed.
The process to get the valid key I used is as follow, I used a pattern serial like 123456789ABCDEFG, launched gdb, breaked on the next character I was searching and then updating the found chars and redoing the whole process.
The instructions were like this:

```bash
0x400a43 <main+167>: cmp    $0x45,%al                # compare AL register to 0x45
```
and

```bash
   0x400a55 <main+185>: movzbl -0x200(%rbp),%eax
   0x400a5c <main+192>: movsbl %al,%edx
   0x400a5f <main+195>: movzbl -0x1f1(%rbp),%eax
   0x400a66 <main+202>: movsbl %al,%eax
   0x400a69 <main+205>: add    %edx,%eax
   0x400a6b <main+207>: cmp    $0x9b,%eax            # compare EAX register to 0x9B
   0x400a70 <main+212>: je     0x400a80 <main+228>
```

The final valid key and the flag are: EZ9dmq4c8g9G7bAV