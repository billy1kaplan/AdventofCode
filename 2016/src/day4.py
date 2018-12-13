# Day 4: Security Through Obscurity


def check_rooms():
    with open('../assets/day4_input.txt') as file:
        lines = file.read().replace('[', '-').replace(']', '').split('\n')

    sector_sum = 0
    for line in lines:
        *ls, sec_s, ck = line.split('-')
        name = ''.join(ls)
        sec = int(sec_s)
        vs = [name.count(c) for c in ck]
        for i in range(1, len(vs)):
            if vs[i] > vs[i - 1] or (vs[i] == vs[i - 1] and ord(ck[i]) < ord(ck[i - 1])):
                break
        else:
            sector_sum += sec
            print('Room:', sec, ' '.join(''.join(chr(97 + ((ord(c) + sec - 97) % 26)) for c in w) for w in ls))
    print('Sum of Valid Rooms:', sector_sum)


if __name__ == '__main__':
    check_rooms()
