# Day 1: No Time for a Taxicab


def part1():
    with open('../assets/day1_input.txt') as file:
        dirs = list(map(lambda x: (1j if x[0] == 'L' else -1j, int(x[1:])), file.read().split(', ')))
    pos = 0
    face = 1j
    for line in dirs:
        face *= line[0]
        pos += face * line[1]

    print('End Location: %d, %d = %d' % (pos.real, pos.imag, absc(pos)))


def part2():
    with open('../assets/day1_input.txt') as file:
        dirs = list(map(lambda x: (1j if x[0] == 'L' else -1j, int(x[1:])), file.read().split(', ')))
    pos = 0
    face = 1j
    visited = {0}
    for line in dirs:
        face *= line[0]
        for s in range(line[1]):
            pos += face
            if pos in visited:
                print('First Repeat %d, %d = %d' % (pos.real, pos.imag, absc(pos)))
                return
            visited.add(pos)


def absc(p: complex):
    return abs(p.real) + abs(p.imag)


if __name__ == '__main__':
    part1()
    part2()
