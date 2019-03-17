# SharifCTF 2016 Serial

This challenge was another great challenge to use angr on. Right off the bad we can see it will be a "find the correct serial number" problem.

```bash
$ file serial
serial: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.26, BuildID[sha1]=77e92e8b1bd4f26641bab4dbf563037a7b9538d2, not stripped 
```

Give it a run:

```bash
$ ./serial 
Please Enter the valid key!
123456
Serial number is not valid!
```
 
Basic. We put in a string and see if it's right. 
Running strings informs us that this is a c++ built binary and we want it to print out "Serial number is valid :)". 
ltrace doesn't give us much to go on. At this point I opened it up in IDA and discovered it was confusing IDA as IDA could not even find the correct main function. 
Well, more correctly IDA was showing it as data rather than code. Further, when running it IDA was complaining about instructions it thought were data being jumped to. 
One of the fun things this binary does is something like:

```bash
.text:0000000000400AFA loc_400AFA:                             ; CODE XREF: .text:0000000000400B00j
.text:0000000000400AFA mov     ax, 5EBh
.text:0000000000400AFE xor     eax, eax
.text:0000000000400B00 jz      short near ptr loc_400AFA+2
```

The problem with that is the "jz" portion. 
Decompilers are not used to "+2" or other strange offsets for the jumps, which is causing even the very good IDA to get confused. 
However, the debugger was obviously able to follow along just fine. 
At that point I stepped through execution until I found the beginning of the input validation:

```bash
.text:0000000000400A19 lea     rax, [rbp-200h]
.text:0000000000400A20 mov     rdi, rax
.text:0000000000400A23 call    _strlen
.text:0000000000400A28 cmp     rax, 10h
.text:0000000000400A2C jz      short loc_400A3C
```

The rbp-200h is our input buffer. 
The first call is checking that the length is 16. The next block looks like:

```bash
.text:0000000000400A3C loc_400A3C:                             ; CODE XREF: .text:0000000000400A2Cj
.text:0000000000400A3C movzx   eax, byte ptr [rbp-200h]
.text:0000000000400A43 cmp     al, 45h ; 'E'
.text:0000000000400A45 jz      short loc_400A55
```
 
So the first character should be an E. 
I could follow it through by hand, writing down the constraints, 
but I wanted to play with angr some more. 
So instead, I single stepped along (setting the ZF manually) until I reached the string telling me that I won. 
For reference, the two important code blocks are:

```bash
.text:0000000000400A3C movzx   eax, byte ptr [rbp-200h]
.text:0000000000400A43 cmp     al, 45h ; 'E'
.text:0000000000400A45 jz      short loc_400A55

.text:0000000000400C5C mov     esi, offset aSerialNumberIs     ; "Serial number is valid :)\n"
```
After verifying that this binary isn't ASLR'd,
I took this information to ask angr for a solution. 
I honestly wasn't sure how well it would do with something like this that has strange offsets,
but it worked like a champ.