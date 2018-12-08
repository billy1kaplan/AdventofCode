# Day 22: Sporifica Virus
from collections import defaultdict


class Virus:
    def __init__(self):
        self.x = self.y = 0
        self.dx = 0
        self.dy = -1

    def tick(self, nodes: set):
        i = False
        if (self.x, self.y) in nodes:
            # Infected Node -> Right Turn
            self.dx, self.dy = -self.dy, self.dx
            nodes.remove((self.x, self.y))
        else:
            # Clean Node -> Left Turn
            self.dx, self.dy = self.dy, -self.dx
            nodes.add((self.x, self.y))
            i = True
        self.x += self.dx
        self.y += self.dy
        return i


class AdvancedVirus:
    def __init__(self):
        self.x = self.y = 0
        self.dx = 0
        self.dy = -1

    def tick(self, nodes: defaultdict):
        i = False
        state = nodes[(self.x, self.y)]
        if state == '#':
            # Infected Node -> Right Turn
            self.dx, self.dy = -self.dy, self.dx
            nodes[(self.x, self.y)] = 'F'
        elif state == 'W':
            # Weakened -> No Turning
            nodes[(self.x, self.y)] = '#'
            i = True
        elif state == 'F':
            # Flagged -> Reverse Direction
            self.dx, self.dy = -self.dx, -self.dy
            nodes[(self.x, self.y)] = '.'
        else:
            # Clean Node -> Left Turn
            self.dx, self.dy = self.dy, -self.dx
            nodes[(self.x, self.y)] = 'W'
        self.x += self.dx
        self.y += self.dy
        return i


def build_map(size: int = 3) -> set:
    # -x <, > +x, /\ -y, \/ +y
    with open('../assets/day22_input.txt') as file:
        lines = file.read().split('\n')
        v = size // 2
        nodes = {(i - v, j - v) for j in range(size) for i in range(size) if lines[j][i] == '#'}
    return nodes


def build_advanced_map(size: int = 25) -> defaultdict:
    nodes = build_map(size)
    adv_nodes = defaultdict(lambda: '.')
    for n in nodes:
        adv_nodes[n] = '#'
    return adv_nodes


def run_virus(max_range, infected, virus):
    ticks = 0
    for i in range(max_range):
        ticks += virus.tick(infected)
    print('Infections:', ticks)


if __name__ == '__main__':
    # Part 1
    run_virus(10000, build_map(25), Virus())
    # Part 2
    run_virus(10000000, build_advanced_map(25), AdvancedVirus())
