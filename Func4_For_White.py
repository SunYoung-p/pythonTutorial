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


def get_mini_mul():
    lcm = 0
    while True:
        lcm += 1
        if lcm % 6 == 0 and lcm % 45 == 0:
            break

    print("6과 45로 나누어 떨어지는 수는 ", lcm, "입니다.")


def get_mini_div():
    val = 0
    gcm = 0

    while True:
        val += 1
        if 42 % val == 0 and 120 % val == 0:
            gcm = val
        if val >= 42:
            break
    print("42와 120의 최대 공약수 : ", gcm)


def print_seven():
    for i in range(1, 11):
        if (7 * i) % 2 == 1:
            continue
        print("7 * ", i, " = ", 7 * i)


def exam_while():
    n = 1
    while n < 100:
        n += 1
        if n % 2 != 0 and n % 3 != 0:
            print(n, end=' ')


