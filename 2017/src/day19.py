# Day 19: A Series of Tubes


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)


def traverse(tubes):

    def get(p: Point):
        if 0 <= p.x < 200 and 0 <= p.y < 200:
            return tubes[p.y][p.x]
        return '.'

    # Coordinates are y, x, Positive y is down, Positive x is right
    p = Point(183, 0)
    d = Point(0, 1)
    items = []
    steps = 0
    while True:
        p += d
        steps += 1
        char = get(p)
        if char == '+':
            if get(p + d) == '.':
                r = Point(d.y, d.x)
                if get(p + r) != '.':
                    d = r
                elif get(p - r) != '.':
                    d = -r
                else:
                    break
        elif char not in ('.', '+', '|', '-'):
            items.append(char)
        elif char == '.':
            break
        if not (0 <= p.x < 200 and 0 <= p.y < 200):
            break
    print('Path: ', ''.join(items), 'Steps: ', steps)


if __name__ == '__main__':
    lines = open('../assets/day19_input.txt').read().split('\n')
    traverse(lines)
