# Day 16: Dancing Programs
from golf.day16 import f as dance_golf


def dance(moves, start='abcdefghijklmnop'):
    pos = list(start)
    for m in moves.split(','):
        if m[0] == 's':
            for i in range(int(m[1:])):
                pos.insert(0, pos.pop())
        elif m[0] == 'x':
            i, j = map(int, m[1:].split('/'))
            pos[i], pos[j] = pos[j], pos[i]
        elif m[0] == 'p':
            i, j = map(lambda x: pos.index(x), m[1:].split('/'))
            pos[i], pos[j] = pos[j], pos[i]
    return ''.join(pos)


def dance_repeat(moves, start='abcdefghijklmnop'):
    pos = list(start)
    cycle = 0
    while True:
        pos = dance(moves, pos)
        cycle += 1
        if pos == start:
            break

    print('Cycle after %d iterations!' % cycle)
    pos = list(start)
    for i in range(1000000000 % cycle):
        pos = dance(moves, pos)
    return pos


if __name__ == '__main__':
    with open('../assets/day16_input.txt') as file:
        lines = file.readline()

    result = dance(lines)
    print('Dance Result: ', result)
    dance_golf(lines)

    print('Billionth Result: ', dance_repeat(lines))
