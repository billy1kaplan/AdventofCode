# Stream Processing


def process_stream():
    with open('assets/day9_input.txt') as file:
        stream = file.read()

    escape = False
    garbage = False
    level = 0
    score = 0
    garbage_count = 0
    for s in stream:
        if garbage:
            if escape:
                escape = False
                continue
            elif s == '!':
                escape = True
            elif s == '>':
                garbage = False
            else:
                garbage_count += 1
        else:
            if s == '<':
                garbage = True
            if s == '{':
                level += 1
            if s == '}':
                score += level
                level -= 1

    print('Score: %d, Amount of Garbage: %d' % (score, garbage_count))


process_stream()
