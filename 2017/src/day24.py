# Day 24: Electromagnetic Moat
import copy


def build_graph():
    edge_set = set()
    with open('../assets/day24_input.txt') as file:
        for line in file:
            ints = list(map(int, line.replace('/', ' ').split()))
            edge_set.add((ints[0], ints[1]))
    return edge_set


def find_strongest(edge_set):
    queue = [Path(0, set())]
    path = 0
    weight = 0
    while queue:
        q = queue.pop()
        for e in edge_set:
            if q.can_append(e):
                p = copy.deepcopy(q)
                p.append(e)
                queue.append(p)
        if q.weight() > weight:
            weight = q.weight()
            path = q
            print('W: %d' % weight, path)
    return path


def find_longest(edge_set):
    queue = [Path(0, set())]
    path = 0
    length = 0
    weight = 0
    while queue:
        q = queue.pop()
        for e in edge_set:
            if q.can_append(e):
                p = copy.deepcopy(q)
                p.append(e)
                queue.append(p)
        if q.length() > length or (q.length() == length and q.weight() > weight):
            weight = q.weight()
            length = q.length()
            path = q
            print('W: %d, L: %d' % (weight, length), path)
    return path


class Path:
    def __init__(self, node, edge_set):
        self.edges = edge_set
        self.node = node

    def append(self, edge):
        self.edges.add(edge)
        if edge[0] == self.node:
            self.node = edge[1]
        else:
            self.node = edge[0]

    def can_append(self, edge):
        return edge not in self.edges and (self.node == edge[0] or self.node == edge[1])

    def weight(self):
        return sum(map(sum, self.edges))

    def length(self):
        return len(self.edges)

    def nodes(self):
        return set(sum(self.edges, ()))

    def __repr__(self):
        return '(' + str(self.node) + ', ' + str(self.weight()) + ') -> ' + str(self.edges)


if __name__ == '__main__':
    edges = build_graph()

    max_path = find_strongest(edges)
    print('Strongest Path: %d = ' % max_path.weight(), max_path)

    best_path = find_longest(edges)
    print('Longest + Strongest: %d = ' % best_path.weight(), best_path)
