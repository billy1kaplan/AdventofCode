# Day 2: Corruption Checksum


def checksum():
    with open('assets/day2_input.txt') as file:
        sum = 0
        for line in file:
            list = [int(i) for i in line.split()]
            sum += max(list) - min(list)

        print(sum)


def checksum_2():
    with open('assets/day2_input.txt') as file:
        result = 0
        for line in file:
            lst = [int(i) for i in line.split()]
            for i, j in ((ii, jj) for ii in lst for jj in lst):
                if i % j == 0 and i != j:
                    result += int(i / j)
                    break

        print(result)