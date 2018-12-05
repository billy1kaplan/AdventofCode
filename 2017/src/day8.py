# Day 8: I Heard you Like Registers


def parse():
    reg = {}
    with open('assets/day8_input.txt') as file:
        max_val = 0
        for line in file:
            parse_line(reg, line.split())
            max_iter = max(reg.values())
            if max_iter > max_val:
                max_val = max_iter
    print('The max value at any point was %d' % max_val)
    return reg


def parse_line(reg, inst):
    if inst[0] not in reg:
        reg[inst[0]] = 0
    if inst[4] not in reg:
        reg[inst[4]] = 0

    val = (1 if inst[1] == 'inc' else -1) * int(inst[2])

    a = reg[inst[4]]
    b = int(inst[6])
    c = inst[5]
    if (c == '>' and a > b) or (c == '<' and a < b) or (c == '<=' and a <= b) or (c == '>=' and a >= b) or (c == '==' and a == b) or (c == '!=' and a != b):
        reg[inst[0]] += val


register = parse()
print(register)
print('Max: %d' % max(register.values()))
