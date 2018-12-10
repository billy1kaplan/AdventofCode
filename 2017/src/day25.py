# Day 25: The Halting Problem


MACHINE = {
    'a': ((1, 1, 'b'), (0, -1, 'c')),
    'b': ((1, -1, 'a'), (1, -1, 'd')),
    'c': ((1, 1, 'd'), (0, 1, 'c')),
    'd': ((0, -1, 'b'), (0, 1, 'e')),
    'e': ((1, 1, 'c'), (1, -1, 'f')),
    'f': ((1, -1, 'e'), (1, 1, 'a'))
}


def checksum():
    tape = set()
    state = 'a'
    slot = 0
    for i in range(12656374):
        cmd = MACHINE[state][slot in tape]
        if cmd[0] == 1:
            tape.add(slot)
        elif slot in tape:
            tape.remove(slot)
        slot += cmd[1]
        state = cmd[2]
    print('Diagnostic Checksum:', len(tape))


if __name__ == '__main__':
    checksum()
