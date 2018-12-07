# Day 20: Particle Swarm
from collections import defaultdict


class Vec3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __lt__(self, other):
        return self.x + self.y + self.z < other.x + other.y + other.z

    def __repr__(self):
        return '(%d, %d, %d)' % (self.x, self.y, self.z)


class Particle:
    def __init__(self, idx: int, p: Vec3, v: Vec3, a: Vec3):
        self.idx = idx
        self.p = p
        self.v = v
        self.a = a

    def iter(self):
        self.v += self.a
        self.p += self.v

    def __lt__(self, other):
        return self.p < other.p

    def __repr__(self):
        return '{%d: p=%s, v=%s, a=%s}' % (self.idx, self.p, self.v, self.a)


def parse(line, idx):
    px, py, pz, vx, vy, vz, ax, ay, az = map(int, ''.join([c if c.isnumeric() or c == '-' else ' ' for c in line]).split())
    return Particle(idx, Vec3(px, py, pz), Vec3(vx, vy, vz), Vec3(ax, ay, az))


def build_particles():
    file = open('../assets/day20_input.txt')
    p = set()
    idx = 0
    for line in file:
        p.add(parse(line, idx))
        idx += 1
    return p


def check_collisions(pars):
    if len(set((p.p.x, p.p.y, p.p.z) for p in pars)) < len(pars):
        collision = defaultdict(set)
        for p in pars:
            collision[p.p.x, p.p.y, p.p.z].add(p)
        for pos, items in collision.items():
            if len(items) > 1:
                for i in items:
                    pars.remove(i)


def part1():
    particles = build_particles()
    for i in range(10000):
        for p in particles:
            p.iter()
    print(min(particles, key=lambda p: p.p.x + p.p.y + p.p.z))


def part2():
    particles = build_particles()
    for i in range(1000):
        for p in particles:
            p.iter()
        check_collisions(particles)
    print(len(particles))


if __name__ == '__main__':
    part2()

