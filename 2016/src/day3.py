# Day 3: Square With Three Sides


def triangles():
    with open('../assets/day3_input.txt') as file:
        ts = [tuple(map(int, line.split())) for line in file.read().split('\n')]
    ts2 = [u for v in [tuple(tuple(j[k] for j in ts[i:i+3]) for k in range(3)) for i in range(0, len(ts), 3)] for u in v]
    rows = sum([1 for t in ts if t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[0] + t[2] > t[1]])
    cols = sum([1 for t in ts2 if t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[0] + t[2] > t[1]])
    print('By Rows:', rows, 'By Cols:', cols)


if __name__ == '__main__':
    triangles()
