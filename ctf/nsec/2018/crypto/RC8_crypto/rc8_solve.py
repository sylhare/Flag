import sage.all
from functools import reduce

'''
int_to_bits  : Given an integer convert it into a list of bits
leak_to_state: Reconstruct a full 64bit state from 8 leaked outputs
pack         : Given two full successive 64 bit states construct a
               list containing their matrix representation.
'''
pack = lambda a, b: [list(map(int, list('{:064b}'.format(a >> n | b << 64 - n & 2**64 - 1)))) for n in range(64)]
leak_to_state = lambda a: reduce(lambda x, y : (x << 8) + y, a[::-1])
int_to_bits = lambda x: [int(c) for c in "{:08b}".format(x)]

# The leaked data from known plaintext (wav header)
s1 = leak_to_state([0xd3, 0xea, 0x3d, 0x6a, 0xfd, 0x66, 0xee, 0x30])
s2 = leak_to_state([0x5f, 0xf4, 0x22, 0x9e, 0xc9, 0xd9, 0x00, 0xc6])

# Build a system of linear equations in GF(2) and solve for the key
A = Matrix(Zmod(2), pack(s1, s2))
b = vector(int_to_bits(s2)[::-1])
key = int(''.join('01'[i] for i in A.solve_right(b)), 2)

print("[+] Seed: {}\n[+] Key: {}".format(s1, key))