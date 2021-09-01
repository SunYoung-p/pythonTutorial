def zero_to_nine():
    n = 0
    while n < 10:
        print(n, end=' ')
        n += 1


def nine_to_zero():
    n = 9
    while n > -1:
        print(n, end=' ')
        n -= 1


def what_number():
    num = 0
    while 3 * num / 2 != 63:
        num += 1
    print(num)
