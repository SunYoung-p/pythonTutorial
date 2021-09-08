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


def double_for():
    for i in range(2, 10):
        for j in range(1, 10):
            print(i * j, end=' ')
        print('')


def to_list(li):
    val = []
    for i in li:
        val.append(i)
    return val


def print_dalpang():
    cnt = 5
    arr = list(range(cnt))

    for i in range(cnt):
        arr[i] = list(range(cnt))

    print(arr)
    cnt_re = int(cnt / 2 + 1)
    for inner_cnt in range(cnt_re):
        # print(inner_cnt) -> 0,1,2
        i = inner_cnt
        j = inner_cnt
        k = 0
        while i <= cnt:
            arr[inner_cnt][i] = 100
            i += 1

    print(' ')


def range_exam_1():
    for i in range(9, 0, -1):
        print(7 * i, end=' ')


def range_exam_2():
    print(tuple(range(1, 101)) + tuple(range(99, 0, -1)))


def def_exam():
    for i in range(3):
        print(i + 1, i + 2, i + 3, sep=', ')  # 1,2,3 과 같이 출력


def call_by_obj(li):
    for i in range(len(li)):
        li[i] += 1  # i = i+1 로 하면 origin list 값이 바뀌지 않는다.  li[idx] 로 직접 참조 필요
