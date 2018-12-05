# Knot Hashing
from golf.day10 import f as knot_hash_golf


def knot_hash(lengths):
    s = 0
    x = 0
    knot = list(range(256))
    for l in lengths:
        knot[:l] = knot[:l][::-1]
        x -= l + s
        for i in range(l + s):
            knot.append(knot.pop(0))
        s += 1
    print(knot[x % len(knot)]*knot[(x + 1) % len(knot)])


def dense_knot_hash(hash_in):
    lengths = to_ascii(hash_in) + [17, 31, 73, 47, 23]
    s = 0
    x = 0
    knot = list(range(256))
    for l in lengths*64:
        knot[:l] = knot[:l][::-1]
        x -= l + s
        for i in range(l + s):
            knot.append(knot.pop(0))
        s += 1

    for _ in range(x%256):
        knot.append(knot.pop(0))

    hashed = ''
    for i in range(16):
        h = 0
        for j in range(16):
            h ^= knot[i*16 + j]
        hashed += '%02x' % h

    return hashed


def to_ascii(string):
    out = []
    for c in string:
        out.append(ord(c))
    return out


if __name__ == '__main__':
    knot_lengths = [147, 37, 249, 1, 31, 2, 226, 0, 161, 71, 254, 243, 183, 255, 30, 70]
    knot_input = '147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70'

    knot_hash(knot_lengths)
    knot_hash_golf(knot_lengths)
    print('Hash: ', dense_knot_hash(knot_input))
