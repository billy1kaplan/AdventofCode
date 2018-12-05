# Digital Plumber
from golf.day12 import c as find_all_connected_golf


def find_all_connected(x=0):
    with open('assets/day12_input.txt') as file:
        lines = list(map(lambda l: list(map(int, ''.join([c if c.isnumeric() else ' ' for c in l]).split())), file.readlines()))

    queue = [x]
    visited = set()
    while queue:
        q = queue.pop()
        for p in lines[q][1:]:
            if p not in visited:
                visited.add(p)
                queue += lines[q][1:]

    return visited


def find_all_groups():
    nodes = set(range(2000))
    groups = 0
    while nodes:
        q = nodes.pop()
        # The same as groups = groups \ visited
        nodes -= find_all_connected(q)
        groups += 1
    print('There are %d groups' % groups)


print('Connected Nodes: %d' % len(find_all_connected()))
find_all_connected_golf(open('assets/day12_input.txt'))

find_all_groups()
