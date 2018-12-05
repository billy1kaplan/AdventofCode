# Day 4: Pass-phrases


def pass_phrases():
    with open('assets/day4_input.txt') as file:
        total = 0
        total_2 = 0
        for line in file:
            words = line.split()
            sorted_words = []

            # Part 2
            for word in words:
                sorted_words.append(''.join(sorted(word)))

            total += is_valid(words)
            total_2 += is_valid(sorted_words)

    print('There are %d, %d valid pass phrases' % (total, total_2))


def is_valid(words):
    for i in range(0, len(words)):
        for j in range(i, len(words)):
            if i == j:
                continue
            if words[i] == words[j]:
                return False
    return True
