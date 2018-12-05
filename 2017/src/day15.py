# Dueling Generators


def duel():
    a = 873
    b = 583
    r = 0
    for i in range(0, 40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        r += a & 65535 == b & 65535
    return r


def duel_2():
    # Test: a = 65, b = 8921
    a = 873
    b = 583
    r = 0
    for i in range(0, 5000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647

        while a & 3 != 0:
            a = (a * 16807) % 2147483647
        while b & 7 != 0:
            b = (b * 48271) % 2147483647

        r += a & 65535 == b & 65535
    return r


if __name__ == '__main__':
    # print('Part 1:', duel())
    print('Part 2:', duel_2())