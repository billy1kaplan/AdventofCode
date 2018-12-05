# Day 11: Hex Ed


def hex_ed():
    with open('assets/day11_input.txt') as file:
        dirs = file.read().split(',')

    pos = Hex()
    dist = 0
    for d in dirs:
        pos.move(d)
        if pos.dist() > dist:
            dist = pos.dist()

    print('Total Distance: %d, Max Distance: %d' % (pos.dist(), dist))


class Hex:
    directions = {
        'n': (0,1,-1), 'nw': (-1,1,0), 'ne': (1,0,-1),
        's': (0,-1,1), 'sw': (-1,0,1), 'se': (1,-1,0)
    }

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def dist(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) // 2

    def move(self, name):
        step = Hex.directions[name]
        self.x += step[0]
        self.y += step[1]
        self.z += step[2]


hex_ed()
