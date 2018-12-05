# Day 1: Inverse Captcha


def inverse_captcha():
    x = input('Enter the capacha: ')
    x += x[0]
    s = 0

    for i in range(0, len(x) - 1):
        if x[i] == x[i + 1]:
            s += int(x[i])


def inverse_captcha_2():
    x = input('Enter the capacha: ')
    s = 0
    j = int(len(x) / 2)

    for i in range(0, len(x)):
        if x[i] == x[(i + j) % len(x)]:
            s += int(x[i])

    print(s)