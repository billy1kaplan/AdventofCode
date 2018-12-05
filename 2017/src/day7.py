# Day 7: Recursive Circus


def find_bottom():
    nodes, weight = parse()

    for name, parent in nodes.items():
        if parent == '':
            return name


def find_unbalanced():
    nodes, weight = parse()
    find_unbalanced_r(nodes, weight, find_bottom())


def find_unbalanced_r(nodes, weight, node):
    children = find_children(nodes, node)
    print('Checking balance of %s - with %d children' % (node, len(children)))
    if children:
        # There are some children
        for child in children:
            find_unbalanced_r(nodes, weight, child)

        print('Calculating balance of %s' % node)
        weights = []
        total_weight = 0
        for child in children:
            total_weight += weight[child]
            weights.append(weight[child])

        if len(set(weights)) == 1:
            # all children are balanced
            weight[node] += total_weight
            print('Node %s is balanced at %d' % (node, total_weight))
        else:
            print('Node %s is not balanced:' % node)
            for w in set(weights):
                if weights.count(w) == 1:
                    # Unbalanced weight obtained
                    print('Weight: %d is unbalanced' % w)
                    bad_child = next(c for c in children if weight[c] == w)
                    w2 = next(x for x in weights if w != x)
                    return parse()[1][bad_child] + w2 - w


def find_children(nodes, node):
    children = []
    for child, parent in nodes.items():
        if parent == node:
            children.append(child)
    return children


def parse():
    with open('assets/day7_input.txt') as file:
        nodes = {} # node name : parent
        weight = {} # node name : weight
        for line in file:
            line = line.replace('(', '').replace(')', '').replace(' ->', '').replace(',','')
            split_lines = line.split()
            name = split_lines.pop(0)
            if name not in nodes:
                nodes[name] = ''
            weight[name] = int(split_lines.pop(0))

            for child in split_lines:
                nodes[child] = name
    return nodes, weight


x = find_unbalanced()
print('')


