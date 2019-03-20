## Serial

Disassemble source of `serial` with radare2.

```assembly
/ (fcn) main 1050
|   int main (int argc, char **argv, char **envp);
|           ; var char *s @ rbp-0x200
|           ; var int var_1ffh @ rbp-0x1ff
|           ; var int var_1feh @ rbp-0x1fe
|           ; var int var_1fdh @ rbp-0x1fd
|           ; var int var_1fch @ rbp-0x1fc
|           ; var int var_1fbh @ rbp-0x1fb
|           ; var int var_1fah @ rbp-0x1fa
|           ; var int var_1f9h @ rbp-0x1f9
|           ; var int var_1f8h @ rbp-0x1f8
|           ; var int var_1f7h @ rbp-0x1f7
|           ; var int var_1f6h @ rbp-0x1f6
|           ; var int var_1f5h @ rbp-0x1f5
|           ; var int var_1f4h @ rbp-0x1f4
|           ; var int var_1f3h @ rbp-0x1f3
|           ; var int var_1f2h @ rbp-0x1f2
|           ; var int var_1f1h @ rbp-0x1f1
|           ; var int var_100h @ rbp-0x100
|           ; DATA XREF from entry0 (0x4008ad)
|           0x0040099c      55             push rbp
|           0x0040099d      4889e5         mov rbp, rsp
|           0x004009a0      4881ec000200.  sub rsp, 0x200
|           0x004009a7      488db500feff.  lea rsi, [s]
|           0x004009ae      b800000000     mov eax, 0
|           0x004009b3      ba20000000     mov edx, 0x20               ; 32
|           0x004009b8      4889f7         mov rdi, rsi
|           0x004009bb      4889d1         mov rcx, rdx
|           0x004009be      f348ab         rep stosq qword [rdi], rax
|           0x004009c1      488db500ffff.  lea rsi, [var_100h]
|           0x004009c8      b800000000     mov eax, 0
|           0x004009cd      ba20000000     mov edx, 0x20               ; 32
|           0x004009d2      4889f7         mov rdi, rsi
|           0x004009d5      4889d1         mov rcx, rdx
|           0x004009d8      f348ab         rep stosq qword [rdi], rax
|           0x004009db  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (+0x45)
|       .-> 0x004009dd      eb05           jmp 0x4009e4
        :   0x004009df      31c0           xor eax, eax
        `=< 0x004009e1      74fa           je 0x4009dd                 ; main+0x41
|           0x004009e3  ~   e8beac0d40     call 0x404db6a6
|           ; CODE XREF from main (0x4009dd)
|           0x004009e4      beac0d4000     mov esi, str.Please_Enter_the_valid_key ; 0x400dac ; "Please Enter the valid key!\n"
|           0x004009e9      bfe0136000     mov edi, obj.std::cout      ; 0x6013e0
|           0x004009ee      e84dfeffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x004009f3  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x4009f9)
|       .-> 0x004009f5      eb05           jmp 0x4009fc
|       :   0x004009f7      31c0           xor eax, eax
|       `=< 0x004009f9      74fa           je 0x4009f5
|           0x004009fb  ~   e8488d8500     call 0xc59748
|           ; CODE XREF from main (0x4009f5)
|           0x004009fc      488d8500feff.  lea rax, [s]
|           0x00400a03      4889c6         mov rsi, rax
|           0x00400a06      bfc0126000     mov edi, obj.std::cin       ; sym..bss ; 0x6012c0
|           0x00400a0b      e850feffff     call sym.std::basic_istream_char_std::char_traits_char___std::operator___char_std::char_traits_char___std::basic_istream_char_std::char_traits_char____char
|           0x00400a10  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x400a16)
|       .-> 0x00400a12      eb05           jmp 0x400a19
|       :   0x00400a14      31c0           xor eax, eax
|       `=< 0x00400a16      74fa           je 0x400a12
|           0x00400a18  ~   e8488d8500     call 0xc59765
|           ; CODE XREF from main (0x400a12)
|           0x00400a19      488d8500feff.  lea rax, [s]
|           0x00400a20      4889c7         mov rdi, rax                ; const char *s
|           0x00400a23      e828feffff     call sym.imp.strlen         ; size_t strlen(const char *s)
|           0x00400a28      4883f810       cmp rax, 0x10               ; 16
|       ,=< 0x00400a2c      740e           je 0x400a3c
|       |   0x00400a2e  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (0x400a34)
|      .--> 0x00400a30      eb05           jmp 0x400a37
|      :|   0x00400a32      31c0           xor eax, eax
|      `==< 0x00400a34      74fa           je 0x400a30
|       |   0x00400a36  ~   e8e93f0200     call 0x424a24
|       |   ; CODE XREF from main (0x400a30)
|       |   0x00400a37      e93f020000     jmp 0x400c7b
|       |   ; CODE XREF from main (0x400a2c)
|       `-> 0x00400a3c      0fb68500feff.  movzx eax, byte [s]
|           0x00400a43      3c45           cmp al, 0x45                ; 'E' ; 69
|       ,=< 0x00400a45      740e           je 0x400a55
|       |   0x00400a47  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (+0xb1)
|      .--> 0x00400a49      eb05           jmp 0x400a50
       :|   0x00400a4b      31c0           xor eax, eax
       `==< 0x00400a4d      74fa           je 0x400a49                 ; main+0xad
|       |   0x00400a4f  ~   e8e9260200     call 0x42313d
|       |   ; CODE XREF from main (0x400a49)
|       |   0x00400a50      e926020000     jmp 0x400c7b
|       |   ; CODE XREF from main (0x400a45)
|       `-> 0x00400a55      0fb68500feff.  movzx eax, byte [s]
|           0x00400a5c      0fbed0         movsx edx, al
|           0x00400a5f      0fb6850ffeff.  movzx eax, byte [var_1f1h]
|           0x00400a66      0fbec0         movsx eax, al
|           0x00400a69      01d0           add eax, edx
|           0x00400a6b      3d9b000000     cmp eax, 0x9b               ; 155
|           0x00400a70      740e           je 0x400a80
|           0x00400a72  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x400a78)
|       .-> 0x00400a74      eb05           jmp 0x400a7b
|       :   0x00400a76      31c0           xor eax, eax
|       `=< 0x00400a78      74fa           je 0x400a74
|           0x00400a7a  ~   e8e9fb0100     call 0x420668
|           ; CODE XREF from main (0x400a74)
|           0x00400a7b      e9fb010000     jmp 0x400c7b
|           0x00400a80      0fb68501feff.  movzx eax, byte [var_1ffh]
|           0x00400a87      3c5a           cmp al, 0x5a                ; 'Z' ; 90
|       ,=< 0x00400a89      740e           je 0x400a99
|       |   0x00400a8b  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (0x400a91)
|      .--> 0x00400a8d      eb05           jmp 0x400a94
|      :|   0x00400a8f      31c0           xor eax, eax
|      `==< 0x00400a91      74fa           je 0x400a8d
|       |   0x00400a93  ~   e8e9e20100     call 0x41ed81
|       |   ; CODE XREF from main (0x400a8d)
|       |   0x00400a94      e9e2010000     jmp 0x400c7b
|       |   ; CODE XREF from main (0x400a89)
|       `-> 0x00400a99      0fb68501feff.  movzx eax, byte [var_1ffh]
|           0x00400aa0      0fbed0         movsx edx, al
|           0x00400aa3      0fb6850efeff.  movzx eax, byte [var_1f2h]
|           0x00400aaa      0fbec0         movsx eax, al
|           0x00400aad      01d0           add eax, edx
|           0x00400aaf      3d9b000000     cmp eax, 0x9b               ; 155
|           0x00400ab4      740e           je 0x400ac4
|           0x00400ab6  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (+0x120)
|       .-> 0x00400ab8      eb05           jmp 0x400abf
        :   0x00400aba      31c0           xor eax, eax
        `=< 0x00400abc      74fa           je 0x400ab8                 ; main+0x11c
|           0x00400abe  ~   e8e9b70100     call 0x41c2ac
|           ; CODE XREF from main (0x400ab8)
|           0x00400abf      e9b7010000     jmp 0x400c7b
|           ; CODE XREF from main (0x400ab4)
|           0x00400ac4      0fb68502feff.  movzx eax, byte [var_1feh]
|           0x00400acb      3c39           cmp al, 0x39                ; '9' ; 57
|       ,=< 0x00400acd      740e           je 0x400add
|       |   0x00400acf  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (+0x139)
|      .--> 0x00400ad1      eb05           jmp 0x400ad8
       :|   0x00400ad3      31c0           xor eax, eax
       `==< 0x00400ad5      74fa           je 0x400ad1                 ; main+0x135
|       |   0x00400ad7  ~   e8e99e0100     call 0x41a9c5
|       |   ; CODE XREF from main (0x400ad1)
|       |   0x00400ad8      e99e010000     jmp 0x400c7b
|       |   ; CODE XREF from main (0x400acd)
|       `-> 0x00400add      0fb68502feff.  movzx eax, byte [var_1feh]
|           0x00400ae4      0fbed0         movsx edx, al
|           0x00400ae7      0fb6850dfeff.  movzx eax, byte [var_1f3h]
|           0x00400aee      0fbec0         movsx eax, al
|           0x00400af1      01d0           add eax, edx
|           0x00400af3      3d9b000000     cmp eax, 0x9b               ; 155
|           0x00400af8      740e           je 0x400b08
|           0x00400afa  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x400b00)
|       .-> 0x00400afc      eb05           jmp 0x400b03
|       :   0x00400afe      31c0           xor eax, eax
|       `=< 0x00400b00      74fa           je 0x400afc
|           0x00400b02  ~   e8e9730100     call 0x417ef0
|           ; CODE XREF from main (0x400afc)
|           0x00400b03      e973010000     jmp 0x400c7b
|           0x00400b08      0fb68503feff.  movzx eax, byte [var_1fdh]
|           0x00400b0f      3c64           cmp al, 0x64                ; 'd' ; 100
|       ,=< 0x00400b11      740e           je 0x400b21
|       |   0x00400b13  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (0x400b19)
|      .--> 0x00400b15      eb05           jmp 0x400b1c
|      :|   0x00400b17      31c0           xor eax, eax
|      `==< 0x00400b19      74fa           je 0x400b15
|       |   0x00400b1b  ~   e8e95a0100     call 0x416609
|       |   ; CODE XREF from main (0x400b15)
|       |   0x00400b1c      e95a010000     jmp 0x400c7b
|       |   ; CODE XREF from main (0x400b11)
|       `-> 0x00400b21      0fb68503feff.  movzx eax, byte [var_1fdh]
|           0x00400b28      0fbed0         movsx edx, al
|           0x00400b2b      0fb6850cfeff.  movzx eax, byte [var_1f4h]
|           0x00400b32      0fbec0         movsx eax, al
|           0x00400b35      01d0           add eax, edx
|           0x00400b37      3d9b000000     cmp eax, 0x9b               ; 155
|           0x00400b3c      740e           je 0x400b4c
|           0x00400b3e  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x400b44)
|       .-> 0x00400b40      eb05           jmp 0x400b47
|       :   0x00400b42      31c0           xor eax, eax
|       `=< 0x00400b44      74fa           je 0x400b40
|           0x00400b46  ~   e8e92f0100     call 0x413b34
|           ; CODE XREF from main (0x400b40)
|           0x00400b47      e92f010000     jmp 0x400c7b
|           0x00400b4c      0fb68504feff.  movzx eax, byte [var_1fch]
|           0x00400b53      3c6d           cmp al, 0x6d                ; 'm' ; 109
|       ,=< 0x00400b55      740e           je 0x400b65
|       |   0x00400b57  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (0x400b5d)
|      .--> 0x00400b59      eb05           jmp 0x400b60
|      :|   0x00400b5b      31c0           xor eax, eax
|      `==< 0x00400b5d      74fa           je 0x400b59
|       |   0x00400b5f  ~   e8e9160100     call 0x41224d
|       |   ; CODE XREF from main (0x400b59)
|       |   0x00400b60      e916010000     jmp 0x400c7b
|       |   ; CODE XREF from main (0x400b55)
|       `-> 0x00400b65      0fb68504feff.  movzx eax, byte [var_1fch]
|           0x00400b6c      0fbed0         movsx edx, al
|           0x00400b6f      0fb6850bfeff.  movzx eax, byte [var_1f5h]
|           0x00400b76      0fbec0         movsx eax, al
|           0x00400b79      01d0           add eax, edx
|           0x00400b7b      3db4000000     cmp eax, 0xb4               ; 180
|       ,=< 0x00400b80      740e           je 0x400b90
|       |   0x00400b82  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (0x400b88)
|      .--> 0x00400b84      eb05           jmp 0x400b8b
|      :|   0x00400b86      31c0           xor eax, eax
|      `==< 0x00400b88      74fa           je 0x400b84
|       |   0x00400b8a  ~   e8e9eb0000     call 0x40f778
|       |   ; CODE XREF from main (0x400b84)
|       |   0x00400b8b      e9eb000000     jmp 0x400c7b
|       |   ; CODE XREF from main (0x400b80)
|       `-> 0x00400b90      0fb68505feff.  movzx eax, byte [var_1fbh]
|           0x00400b97      3c71           cmp al, 0x71                ; 'q' ; 113
|       |   0x00400b99      740e           je 0x400ba9
|       |   0x00400b9b  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (0x400ba1)
|      .--> 0x00400b9d      eb05           jmp 0x400ba4
|      :|   0x00400b9f      31c0           xor eax, eax
|      `==< 0x00400ba1      74fa           je 0x400b9d
|       |   0x00400ba3  ~   e8e9d20000     call 0x40de91
|       |   ; CODE XREF from main (0x400b9d)
|       |   0x00400ba4      e9d2000000     jmp 0x400c7b
|       |   ; CODE XREF from main (0x400b99)
|       |   0x00400ba9      0fb68505feff.  movzx eax, byte [var_1fbh]
|       |   0x00400bb0      0fbed0         movsx edx, al
|       |   0x00400bb3      0fb6850afeff.  movzx eax, byte [var_1f6h]
|       |   0x00400bba      0fbec0         movsx eax, al
|       |   0x00400bbd      01d0           add eax, edx
|       |   0x00400bbf      3daa000000     cmp eax, 0xaa               ; 170
|       |   0x00400bc4      740e           je 0x400bd4
|       |   0x00400bc6  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (+0x230)
|      .--> 0x00400bc8      eb05           jmp 0x400bcf
       :|   0x00400bca      31c0           xor eax, eax
       `==< 0x00400bcc      74fa           je 0x400bc8                 ; main+0x22c
|       |   0x00400bce  ~   e8e9a70000     call 0x40b3bc
|       |   ; CODE XREF from main (0x400bc8)
|       |   0x00400bcf      e9a7000000     jmp 0x400c7b
|       |   0x00400bd4      0fb68506feff.  movzx eax, byte [var_1fah]
|       |   0x00400bdb      3c34           cmp al, 0x34                ; '4' ; 52
|      ,==< 0x00400bdd      740e           je 0x400bed
|      ||   0x00400bdf  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|      ||   ; CODE XREF from main (+0x249)
|     .---> 0x00400be1      eb05           jmp 0x400be8
      :||   0x00400be3      31c0           xor eax, eax
      `===< 0x00400be5      74fa           je 0x400be1                 ; main+0x245
|      ||   0x00400be7  ~   e8e98e0000     call 0x409ad5
|      ||   ; CODE XREF from main (0x400be1)
|      ||   0x00400be8      e98e000000     jmp 0x400c7b
|      ||   ; CODE XREF from main (0x400bdd)
|      `--> 0x00400bed      0fb68506feff.  movzx eax, byte [var_1fah]
|       |   0x00400bf4      0fbed0         movsx edx, al
|       |   0x00400bf7      0fb68509feff.  movzx eax, byte [var_1f7h]
|       |   0x00400bfe      0fbec0         movsx eax, al
|       |   0x00400c01      01d0           add eax, edx
|       |   0x00400c03      3d9b000000     cmp eax, 0x9b               ; 155
|       |   0x00400c08      740b           je 0x400c15
|       |   0x00400c0a  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (0x400c10)
|      .--> 0x00400c0c      eb05           jmp 0x400c13
|      :|   ; CODE XREF from main (0x400b98)
|      :`-> 0x00400c0e      31c0           xor eax, eax
|      `==< 0x00400c10      74fa           je 0x400c0c
|           0x00400c12  ~   e8eb660fb6     call 0xffffffffb64f7302
|           ; CODE XREF from main (0x400c0c)
|           0x00400c13      eb66           jmp 0x400c7b
|           ; CODE XREF from main (0x400c08)
|           0x00400c15      0fb68507feff.  movzx eax, byte [var_1f9h]
|           0x00400c1c      3c63           cmp al, 0x63                ; 'c' ; 99
|       ,=< 0x00400c1e      740b           je 0x400c2b
|       |   0x00400c20  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|       |   ; CODE XREF from main (0x400c26)
|      .--> 0x00400c22      eb05           jmp 0x400c29
|      :|   0x00400c24      31c0           xor eax, eax
|      `==< 0x00400c26      74fa           je 0x400c22
|       |   0x00400c28  ~   e8eb500fb6     call 0xffffffffb64f5d18
|       |   ; CODE XREF from main (0x400c22)
|       |   0x00400c29      eb50           jmp 0x400c7b
|       |   ; CODE XREF from main (0x400c1e)
|       `-> 0x00400c2b      0fb68507feff.  movzx eax, byte [var_1f9h]
|           0x00400c32      0fbed0         movsx edx, al
|           0x00400c35      0fb68508feff.  movzx eax, byte [var_1f8h]
|           0x00400c3c      0fbec0         movsx eax, al
|           0x00400c3f      01d0           add eax, edx
|           0x00400c41      3d9b000000     cmp eax, 0x9b               ; 155
|           0x00400c46      740b           je 0x400c53
|           0x00400c48  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x400c4e)
|       .-> 0x00400c4a      eb05           jmp 0x400c51
|       :   0x00400c4c      31c0           xor eax, eax
|       `=< 0x00400c4e      74fa           je 0x400c4a
|           0x00400c50  ~   e8eb2866b8     call 0xffffffffb8a63540
|           ; CODE XREF from main (0x400c4a)
|           0x00400c51      eb28           jmp 0x400c7b
|           0x00400c53  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x400c59)
|      ,.-> 0x00400c55      eb05           jmp 0x400c5c
|      |:   0x00400c57      31c0           xor eax, eax
|      |`=< 0x00400c59      74fa           je 0x400c55
|      |    0x00400c5b  ~   e8bec90d40     call 0x404dd61e
|      |    ; CODE XREF from main (0x400c55)
|      `--> 0x00400c5c      bec90d4000     mov esi, str.Serial_number_is_valid_: ; 0x400dc9 ; "Serial number is valid :)\n"
|           0x00400c61      bfe0136000     mov edi, obj.std::cout      ; 0x6013e0
|           0x00400c66      e8d5fbffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x00400c6b  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x400c71)
|       .-> 0x00400c6d      eb05           jmp 0x400c74
|       :   0x00400c6f      31c0           xor eax, eax
|       `=< 0x00400c71      74fa           je 0x400c6d
|           0x00400c73  ~   e8b8000000     call fcn.00400d30           ; sym.__libc_csu_init+0x20
|           ; CODE XREF from main (0x400c6d)
|           0x00400c74      b800000000     mov eax, 0
|           0x00400c79      eb26           jmp 0x400ca1
|           ; XREFS: CODE 0x00400a37  CODE 0x00400a50  CODE 0x00400a7b  CODE 0x00400a94  CODE 0x00400abf
|           ; XREFS: CODE 0x00400ad8  CODE 0x00400b03  CODE 0x00400b1c  CODE 0x00400b47  CODE 0x00400b60
|           ; XREFS: CODE 0x00400b8b  CODE 0x00400ba4  CODE 0x00400bcf  CODE 0x00400be8  CODE 0x00400c13
|           ; XREFS: CODE 0x00400c29  CODE 0x00400c51
|           0x00400c7b  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x400c81)
|       .-> 0x00400c7d      eb05           jmp 0x400c84
|       :   0x00400c7f      31c0           xor eax, eax
|       `=< 0x00400c81      74fa           je 0x400c7d
|           0x00400c83  ~   e8bee40d40     call 0x404df146
|           ; CODE XREF from main (0x400c7d)
|           0x00400c84      bee40d4000     mov esi, str.Serial_number_is_not_valid ; 0x400de4 ; "Serial number is not valid!\n"
|           0x00400c89      bfe0136000     mov edi, obj.std::cout      ; 0x6013e0
|           0x00400c8e      e8adfbffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x00400c93  ~   66b8eb05       mov ax, 0x5eb               ; 1515
|           ; CODE XREF from main (0x400c99)
|       .-> 0x00400c95      eb05           jmp 0x400c9c
|       :   0x00400c97      31c0           xor eax, eax
|       `=< 0x00400c99      74fa           je 0x400c95
|           0x00400c9b  ~   e8b8000000     call fcn.00400d58           ; sym.__libc_csu_init+0x48
|           ; CODE XREF from main (0x400c95)
|           0x00400c9c      b800000000     mov eax, 0
|           ; CODE XREF from main (0x400c79)
|           0x00400ca1      eb08           jmp 0x400cab
..
|           ; CODE XREF from main (0x400ca1)
|           0x00400cab      c9             leave
\           0x00400cac      c3             ret
..
            ;-- _GLOBAL__sub_I_main:
|           ;-- fcn.00400d58:
            ;-- section..fini:
            ;-- .fini:
```