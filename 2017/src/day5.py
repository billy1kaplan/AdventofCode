# Day 5: A maze of twisty trampolines, all alike


def trampoline():
    with open('assets/day5_input.txt') as file:
        steps = []
        for line in file:
            steps.append(int(line))

        # Test: should take 5 jumps on part 1, 10 on part 2
        # steps = [0, 3, 0, 1, -3]

        i = 0
        jumps = 0
        while 0 <= i < len(steps):
            # for part 2, set this to constant 1
            step = 1 if steps[i] < 3 else -1
            steps[i] += step
            i += steps[i] - step
            jumps += 1
    print('Took %d jumps to exit the maze!' % jumps)
