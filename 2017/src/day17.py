# Day 17: Spinlock
from golf.day17 import f as spinlock_golf, g as spinlock_fast_golf


def spinlock(step, level=2018):
    buffer = [0]
    pos = -1
    for i in range(1, level):
        pos = (pos + step + 1) % i
        buffer.insert(pos + 1, i)
    return buffer, pos


def fast_spinlock(step, level=2018):
    item = 0
    pos = -1
    for i in range(1, level):
        pos = (pos + step + 1) % i
        if pos == 0:
            item = i
    return item


if __name__ == '__main__':
    max_level = 2018
    spin, idx = spinlock(349)
    print('After Last: %d, After 0: %d' % (spin[(idx + 2) % max_level], spin[1]))

    fast = fast_spinlock(349, 50000000)
    print('After Last: %d' % fast)

    print('Golfed Part 1: %d, Golfed Part 2: %d' % (spinlock_golf(349), spinlock_fast_golf(349)))
