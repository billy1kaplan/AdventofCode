# Day 23: Coprocessor Conflagration
from collections import defaultdict
from math import sqrt
from itertools import count, islice


class Assembly:
    def __init__(self, ast):
        self.ast = ast
        self.reg = defaultdict(int)
        self.pos = 0
        self.mul_counter = 0

    def val(self, x) -> int:
        return x if isinstance(x, int) else self.reg[x]

    def set(self, r, x):
        self.reg[r] = self.val(x)

    def sub(self, r, x):
        self.reg[r] -= self.val(x)

    def mul(self, r, x):
        self.reg[r] *= self.val(x)
        self.mul_counter += 1

    def jnz(self, x, y):
        if self.val(x) != 0:
            self.pos += self.val(y) - 1

    def run(self):
        while 0 <= self.pos < len(self.ast):
            exec(self.ast[self.pos])
            self.pos += 1


def build():
    def build_line(l) -> str:
        ls = l.split()
        return 'self.%s(%s, %s)' % (ls[0], build_int(ls[1]), build_int(ls[2]))

    def build_int(i) -> str:
        try:
            int(i)
            return i
        except ValueError:
            return '\'%s\'' % i

    with open('../assets/day23_input.txt') as file:
        ast = tuple(tuple(build_line(line) for line in file.read().split('\n')))
    return ast


def part1():
    exe = Assembly(build())
    exe.run()
    print(exe.mul_counter)


def part2():
    b = 107900
    h = 0
    while b <= 124900:
        h += 1 - prime(b)
        b += 17
    print('h = %d' % h)


def prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


if __name__ == '__main__':
    part1()
    part2()
