 ## Reverse Engineered serial
 
 This is a mini simplified version
 
 ```assembly
            ;-- main:
            ;-- section.0.__TEXT.__text:
            ;-- _main:
            ;-- func.100000e60:
            ;-- rip:
/ (fcn) entry0 232
|   entry0 ();
|           ; var int var_20h @ rbp-0x20
|           ; var int var_1ch @ rbp-0x1c
|           ; var int var_18h @ rbp-0x18
|           ; var int var_14h @ rbp-0x14
|           ; var char *s @ rbp-0x10
|           ; var char *var_4h @ rbp-0x4
|           0x100000e60      55             push rbp                   ; [00] -r-x section size 232 named 0.__TEXT.__text
|           0x100000e61      4889e5         mov rbp, rsp
|           0x100000e64      4883ec20       sub rsp, 0x20
|           0x100000e68      488d3d1b0100.  lea rdi, str.Enter_input:  ; section.3.__TEXT.__cstring ; 0x100000f8a ; "Enter input: " ; const char *format
|           0x100000e6f      c745fc000000.  mov dword [var_4h], 0
|           0x100000e76      b000           mov al, 0
|           0x100000e78      e8cb000000     call sym.imp.printf        ; int printf(const char *format)
|           0x100000e7d      488d3d140100.  lea rdi, [0x100000f98]     ; "%s" ; 4294971288 ; const char *format
|           0x100000e84      488b75f0       mov rsi, qword [s]
|           0x100000e88      8945ec         mov dword [var_14h], eax
|           0x100000e8b      b000           mov al, 0
|           0x100000e8d      e8bc000000     call sym.imp.scanf         ; int scanf(const char *format)
|           0x100000e92      488b7df0       mov rdi, qword [s]         ; const char *s
|           0x100000e96      8945e8         mov dword [var_18h], eax
|           0x100000e99      e8b6000000     call sym.imp.strlen        ; size_t strlen(const char *s)
|           0x100000e9e      4883f804       cmp rax, 4                 ; 4
|       ,=< 0x100000ea2      0f8581000000   jne 0x100000f29
|       |   0x100000ea8      488b45f0       mov rax, qword [s]
|       |   0x100000eac      0fbe08         movsx ecx, byte [rax]
|       |   0x100000eaf      83f945         cmp ecx, 0x45              ; 'E' ; 69
|      ,==< 0x100000eb2      0f856c000000   jne 0x100000f24
|      ||   0x100000eb8      488b45f0       mov rax, qword [s]
|      ||   0x100000ebc      0fbe08         movsx ecx, byte [rax]
|      ||   0x100000ebf      488b45f0       mov rax, qword [s]
|      ||   0x100000ec3      0fbe5003       movsx edx, byte [rax + 3]  ; [0x3:1]=255 ; 3
|      ||   0x100000ec7      01d1           add ecx, edx
|      ||   0x100000ec9      81f99b000000   cmp ecx, 0x9b              ; 155
|     ,===< 0x100000ecf      0f854a000000   jne 0x100000f1f
|     |||   0x100000ed5      488b45f0       mov rax, qword [s]
|     |||   0x100000ed9      0fbe4801       movsx ecx, byte [rax + 1]  ; [0x1:1]=255 ; 1
|     |||   0x100000edd      83f95a         cmp ecx, 0x5a              ; 'Z' ; 90
|    ,====< 0x100000ee0      0f8534000000   jne 0x100000f1a
|    ||||   0x100000ee6      488b45f0       mov rax, qword [s]
|    ||||   0x100000eea      0fbe4801       movsx ecx, byte [rax + 1]  ; [0x1:1]=255 ; 1
|    ||||   0x100000eee      488b45f0       mov rax, qword [s]
|    ||||   0x100000ef2      0fbe5002       movsx edx, byte [rax + 2]  ; [0x2:1]=255 ; 2
|    ||||   0x100000ef6      01d1           add ecx, edx
|    ||||   0x100000ef8      81f99b000000   cmp ecx, 0x9b              ; 155
|   ,=====< 0x100000efe      0f8511000000   jne 0x100000f15
|   |||||   0x100000f04      488d3d900000.  lea rdi, str.success       ; 0x100000f9b ; "success!\n" ; const char *format
|   |||||   0x100000f0b      b000           mov al, 0
|   |||||   0x100000f0d      e836000000     call sym.imp.printf        ; int printf(const char *format)
|   |||||   0x100000f12      8945e4         mov dword [var_1ch], eax
|   |||||   ; CODE XREF from entry0 (0x100000efe)
|  ,`-----> 0x100000f15      e900000000     jmp 0x100000f1a
|  | ||||   ; CODE XREFS from entry0 (0x100000ee0, 0x100000f15)
|  `,`----> 0x100000f1a      e900000000     jmp 0x100000f1f
|   | |||   ; CODE XREFS from entry0 (0x100000ecf, 0x100000f1a)
|   `,`---> 0x100000f1f      e900000000     jmp 0x100000f24
|    | ||   ; CODE XREFS from entry0 (0x100000eb2, 0x100000f1f)
|    `,`--> 0x100000f24      e900000000     jmp 0x100000f29
|     | |   ; CODE XREFS from entry0 (0x100000ea2, 0x100000f24)
|     `-`-> 0x100000f29      488d3d750000.  lea rdi, str.Your_input_is__s ; 0x100000fa5 ; "\nYour input is %s\n" ; const char *format
|           0x100000f30      488b75f0       mov rsi, qword [s]
|           0x100000f34      b000           mov al, 0
|           0x100000f36      e80d000000     call sym.imp.printf        ; int printf(const char *format)
|           0x100000f3b      31c9           xor ecx, ecx
|           0x100000f3d      8945e0         mov dword [var_20h], eax
|           0x100000f40      89c8           mov eax, ecx
|           0x100000f42      4883c420       add rsp, 0x20
|           0x100000f46      5d             pop rbp
\           0x100000f47      c3             ret
```