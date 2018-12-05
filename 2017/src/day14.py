# Day 14: Disc Defragmentation (And Knot Hashing!)
from src.day10 import dense_knot_hash


def defrag():
    cells = []
    for i in range(128):
        hash_out = dense_knot_hash(HASH_KEY + '-' + str(i))
        row = []
        for c in hash_out:
            row += HASH_LOOKUP[c]
        cells.append(row)
    return cells


def regions(cells, size=128):
    points = [(x,y) for x in range(size) for y in range(size) if cells[x][y]]
    queue = []
    num_regions = 0
    while points:
        queue.append(points.pop())
        num_regions += 1
        while queue:
            p = queue.pop()
            for c in CARDINALS:
                q = p[0]+c[0], p[1]+c[1]
                if q in points:
                    queue.append(q)
                    points.remove(q)
    return num_regions


def vec_add(p, q):
    return p[0] + q[0], p[1] + q[1]


CARDINALS = {(0, 1), (0, -1), (1, 0), (-1, 0)}
HASH_KEY = 'ljoxqyyw'
HASH_LOOKUP = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'a': [1, 0, 1, 0],
    'b': [1, 0, 1, 1],
    'c': [1, 1, 0, 0],
    'd': [1, 1, 0, 1],
    'e': [1, 1, 1, 0],
    'f': [1, 1, 1, 1]
}

if __name__ == '__main__':
    disc = defrag()
    print('Used Disc Space:', sum(sum(disc, [])))
    print('Regions: ', regions(disc))
