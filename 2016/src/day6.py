# Day 6: Signals and Noise
from collections import defaultdict


def error_correct(size: int = 8):
    chars = [defaultdict(int) for _ in range(size)]
    with open('../assets/day6_input.txt') as file:
        for line in file.read().split('\n'):
            for i in range(len(line)):
                chars[i][line[i]] += 1

    part1 = ''.join(max(chars[i].items(), key=lambda x: x[1])[0] for i in range(size))
    part2 = ''.join(min(chars[i].items(), key=lambda x: x[1])[0] for i in range(size))
    print(part1, part2)


if __name__ == '__main__':
    error_correct()
