#!/usr/bin/env python3
import sys

def rc8(state, key, n):
    '''
    Top Secret RC8 Stream Cipher
    '''
    while (n > 0):
        yield state & 0xff
        for _ in range(8):
            c, s = key, state
            b = 0
            while c:
                b ^= c & 1 * s & 1
                c >>= 1 ; s >>= 1
            state = state >> 1 | b << 63
        n -= 1

def main():
    seed, key = ?, ? # Missing

    with open(sys.argv[1], 'rb') as fin:
        data = bytearray(fin.read())

    for i,x in enumerate(rc8(seed, key, len(data))):
        data[i] ^= x

    with open(sys.argv[1] + '.enc', 'wb') as fout:
        fout.write(data)

if __name__ == "__main__":
    main()