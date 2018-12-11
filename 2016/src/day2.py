# Day 2: Bathroom Security


def code(s: str, p: complex = 0):
    for c in s:
        p += DIR_MAP[c]
        p = clamp(p.real) + clamp(p.imag) * 1j
    return p


def code2(s: str, p: complex = 0):
    for c in s:
        if p + DIR_MAP[c] in KEY_MAP.keys():
            p += DIR_MAP[c]
    return p


def key(i: complex):
    return 5 + i.real - 3 * i.imag


def clamp(i: float):
    return max(-1.0, min(1.0, i))


DIR_MAP = {
    'D': -1j,
    'U': 1j,
    'L': -1,
    'R': 1
}

KEY_MAP = {
    2j: 1,
    -1 + 1j: 2,
    1j: 3,
    1 + 1j: 4,
    -2: 5,
    -1: 6,
    0: 7,
    1: 8,
    2: 9,
    -1 - 1j: 'A',
    -1j: 'B',
    1 - 1j: 'C',
    -2j: 'D'
}

if __name__ == '__main__':
    pos1 = 0 + 0j
    pos2 = -2 + 0j
    for word in open('../assets/day2_input.txt').read().split('\n'):
        pos1 = code(word, pos1)
        pos2 = code2(word, pos2)
        print('Keys: ', key(pos1), KEY_MAP[pos2])
