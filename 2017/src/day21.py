# Day 21: Fractal Art


def create_from(gen: str) -> tuple:
    return tuple(tuple(i) for i in gen.split('/'))


def rotate(m: tuple) -> tuple:
    return tuple(tuple(i[j] for i in m)[::-1] for j in range(len(m)))


def flip(m: tuple) -> tuple:
    return m[::-1]


def splice(m: tuple) -> tuple:
    size = len(m)
    p = (3, 2)[size % 2 == 0]
    return tuple(tuple(tuple(tuple(m[p*j + y][p*i + x] for x in range(p)) for y in range(p)) for i in range(size // p)) for j in range(size // p))


def repair(m: tuple) -> tuple:
    return tuple(u for v in tuple(tuple(tuple(j for i in tuple(q[k][:] for q in p) for j in i) for k in range(len(m[0][0]))) for p in m) for u in v)


def build_rules() -> dict:
    r = {}
    with open('../assets/day21_input.txt') as file:
        for line in file:
            inp, out = map(create_from, line.replace('\n', '').split(' => '))
            for i in range(4):
                r[inp] = out
                r[flip(inp)] = out
                inp = rotate(inp)
    return r


def fractal_iter(m: tuple, r: dict) -> tuple:
    return repair(tuple(tuple(r[i] for i in j) for j in splice(m)))


def iterate(r: dict, amount: int = 5):
    art = create_from('.#./..#/###')
    for _ in range(amount):
        art = fractal_iter(art, r)
    print(sum(map(lambda x: x.count('#'), art)))


if __name__ == '__main__':
    rules = build_rules()
    iterate(rules)
    iterate(rules, 18)
