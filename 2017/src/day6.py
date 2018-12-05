# Day 6: Memory Reallocation


def memory_reallocation():
    found = []
    banks = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
    total = 0
    length = len(banks)

    while banks not in found:
        found.append(banks.copy())

        total += 1
        i = max_i(banks)
        val = banks[i]
        banks[i] = 0
        for j in range(1 + i, 1 + i + val):
            banks[j % length] += 1

    print('Took %d tries before infinite loop' % total)

    start = 0
    for i in range(len(found) - 1):
        if found[i] == banks:
            start = i

    print('Total loop length is %d' % (total - start))



def max_i(list):
    max_value = max(list)
    for i in range(len(list)):
        if list[i] == max_value:
            return i
    return 0


memory_reallocation()
