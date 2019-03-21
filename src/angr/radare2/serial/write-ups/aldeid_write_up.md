# SharifCTF-2016/serial

Source: https://www.aldeid.com/wiki/SharifCTF-2016/serial

## Analysis
### Running the executable
When launched, the program asks for a serial number and displays an error message if the serial is invalid:

$ ./serial 
Please Enter the valid key!
123456
Serial number is not valid!

### Anti-disassembly
This challenge is all about reorganizing code blocks in IDA-Pro because it makes use of anti-disassembly techniques. 
Once reorganized, it becomes relatively easy to find the serial.

### Checking serial length
First of all, the serial length is checked and should be 16 characters long:

```assembly
.text:0000000000400A19                 lea     rax, [rbp+serial_00]
.text:0000000000400A20                 mov     rdi, rax        ; s
.text:0000000000400A23                 call    _strlen
.text:0000000000400A28                 cmp     rax, 10h        ; len(serial) = 16
.text:0000000000400A2C                 jz      short loc_400A3C
```

### Checking characters of serial
Then, each character is checked. Below is the sanitized code:

```assembly
.text:0000000000400A3C                 movzx   eax, [rbp+serial_00]
.text:0000000000400A43                 cmp     al, 45h         ; serial[0] = 'E'
.text:0000000000400A45                 jz      short loc_400A55
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400A55                 movzx   eax, [rbp+serial_00]
.text:0000000000400A5C                 movsx   edx, al         ; edx = serial[0] = 0x45
.text:0000000000400A5F                 movzx   eax, [rbp+serial_15]
.text:0000000000400A66                 movsx   eax, al         ; eax = serial[15]
.text:0000000000400A69                 add     eax, edx
.text:0000000000400A6B                 cmp     eax, 9Bh        ; serial[15] = 0x9B - 0x45 = 'V'
.text:0000000000400A70                 jz      short loc_400A80
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400A80                 movzx   eax, [rbp+serial_01]
.text:0000000000400A87                 cmp     al, 5Ah         ; serial[1] = 'Z'
.text:0000000000400A89                 jz      short loc_400A99
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400A99                 movzx   eax, [rbp+serial_01]
.text:0000000000400AA0                 movsx   edx, al         ; edx = serial[1] = 0x5A
.text:0000000000400AA3                 movzx   eax, [rbp+serial_14]
.text:0000000000400AAA                 movsx   eax, al         ; eax = serial[14]
.text:0000000000400AAD                 add     eax, edx
.text:0000000000400AAF                 cmp     eax, 9Bh        ; serial[14] = 0x9B - 0x5A = 'A'
.text:0000000000400AB4                 jz      short loc_400AC4
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400AC4                 movzx   eax, [rbp+serial_02]
.text:0000000000400ACB                 cmp     al, 39h         ; serial[2] = '9'
.text:0000000000400ACD                 jz      short loc_400ADD
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400ADD                 movzx   eax, [rbp+serial_02]
.text:0000000000400AE4                 movsx   edx, al         ; edx = serial[2] = 0x39
.text:0000000000400AE7                 movzx   eax, [rbp+serial_13]
.text:0000000000400AEE                 movsx   eax, al         ; eax = serial[13]
.text:0000000000400AF1                 add     eax, edx
.text:0000000000400AF3                 cmp     eax, 9Bh        ; serial[13] = 0x9B - 0x39 = 'b'
.text:0000000000400AF8                 jz      short loc_400B08
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400B08                 movzx   eax, [rbp+serial_03]
.text:0000000000400B0F                 cmp     al, 64h         ; serial[3] = 'd'
.text:0000000000400B11                 jz      short loc_400B21
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400B21                 movzx   eax, [rbp+serial_03]
.text:0000000000400B28                 movsx   edx, al         ; edx = serial[3] = 0x64
.text:0000000000400B2B                 movzx   eax, [rbp+serial_12]
.text:0000000000400B32                 movsx   eax, al         ; eax = serial[12]
.text:0000000000400B35                 add     eax, edx
.text:0000000000400B37                 cmp     eax, 9Bh        ; serial[12] = 0x9B - 0x64 = '7'
.text:0000000000400B3C                 jz      short loc_400B4C
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400B4C                 movzx   eax, [rbp+serial_04]
.text:0000000000400B53                 cmp     al, 6Dh         ; serial[4] = 'm'
.text:0000000000400B55                 jz      short loc_400B65
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400B65                 movzx   eax, [rbp+serial_04]
.text:0000000000400B6C                 movsx   edx, al         ; edx = serial[4] = 0x6D
.text:0000000000400B6F                 movzx   eax, [rbp+serial_11]
.text:0000000000400B76                 movsx   eax, al         ; eax = serial[11]
.text:0000000000400B79                 add     eax, edx
.text:0000000000400B7B                 cmp     eax, 0B4h       ; serial[11] = 0xB4 - 0x6D = 'G'
.text:0000000000400B80                 jz      short loc_400B90
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400B90                 movzx   eax, [rbp+serial_05]
.text:0000000000400B97                 cmp     al, 71h         ; serial[5] = 'q'
.text:0000000000400B99                 jz      short loc_400BA9
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400BA9                 movzx   eax, [rbp+serial_05]
.text:0000000000400BB0                 movsx   edx, al         ;  edx = serial[5] = 0x71
.text:0000000000400BB3                 movzx   eax, [rbp+serial_10]
.text:0000000000400BBA                 movsx   eax, al         ; eax = serial[10]
.text:0000000000400BBD                 add     eax, edx
.text:0000000000400BBF                 cmp     eax, 0AAh       ; serial[10] = 0xAA - 0x71 = '9'
.text:0000000000400BC4                 jz      short loc_400BD4
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400BD4                 movzx   eax, [rbp+serial_06]
.text:0000000000400BDB                 cmp     al, 34h         ; serial[6] = '4'
.text:0000000000400BDD                 jz      short loc_400BED
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400BED                 movzx   eax, [rbp+serial_06]
.text:0000000000400BF4                 movsx   edx, al         ;  edx = serial[4] = 0x34
.text:0000000000400BF7                 movzx   eax, [rbp+serial_09]
.text:0000000000400BFE                 movsx   eax, al         ; eax = serial[9]
.text:0000000000400C01                 add     eax, edx
.text:0000000000400C03                 cmp     eax, 9Bh        ; serial[9] = 0x9B - 0x34 = 'g'
.text:0000000000400C08                 jz      short loc_400C15
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400C15                 movzx   eax, [rbp+serial_07]
.text:0000000000400C1C                 cmp     al, 63h         ; serial[7] = 'c'
.text:0000000000400C1E                 jz      short loc_400C2B
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400C2B                 movzx   eax, [rbp+serial_07]
.text:0000000000400C32                 movsx   edx, al         ; edx = serial[7] = 0x63
.text:0000000000400C35                 movzx   eax, [rbp+serial_08]
.text:0000000000400C3C                 movsx   eax, al         ; eax = serial[8]
.text:0000000000400C3F                 add     eax, edx
.text:0000000000400C41                 cmp     eax, 9Bh        ; serial[8] = 0x9B - 0x63 = '8'
.text:0000000000400C46                 jz      short near ptr unk_400C53
; ----- [SNIP] ---------------------------------------------------------------------------
.text:0000000000400C5C loc_400C5C:
.text:0000000000400C5C                 mov     esi, offset aSerialNumberIs ; "Serial number is valid :)\n"
.text:0000000000400C61                 mov     edi, offset _ZSt4cout@@GLIBCXX_3_4
.text:0000000000400C66                 call    __ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc ; std::operator<<<std::char_traits<char>>(std::basic_ostream<char,std::char_traits<char>> &,char const*)
.text:0000000000400C66 ; ---------------------------------------------------------------------------
```

## Solution
This eventually leads to the following serial number: EZ9dmq4c8g9G7bAV. Let's check:

```assembly
$ ./serial 
Please Enter the valid key!
EZ9dmq4c8g9G7bAV
Serial number is valid :)
```