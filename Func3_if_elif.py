def is_zero(n):
    if n >= 0:
        print("입력한 값은 0이거나 0보다 큽니다")
    else:
        print("입력 한 값은 0보다 작습니다")


def is_one(n):
    if 0 < n < 2:  # 2개 이상의 부등식을 조합하여 사용 가능하다
        print("입력한 값은 1 입니다")
    else:
        print("입력 한 값은 1이 아닙니다")


def what_size(n):
    if n < 3 or n > 10:
        print(n, "은 3보다 작거나 10보다 큽니다")
    else:
        print(n, "은 3보다 작지 않거나 10보다 크지 않습니다")


def what_multi(n):
    if n % 2 == 0:
        if n % 3 == 0:
            print(n, "은 2의 배수이고 3의 배수이다")
        else:
            print(n, "은 2의 배수이고 3의 배수가 아니다")
    elif n % 3 == 0:
        if n % 2 == 0:
            print(n, "은 2의 배수이고 3의 배수이다")
        else:
            print(n, "은 3의 배수이고 2의 배수가 아니다")
    else:
        print(n, "은 2의 배수도 3의 배수도 아니다")


def what_size_two(n):
    if n < 0:
        print("입력한 값은 0 보다 작습니다.")
    elif 0 <= n < 10:
        print("입력한 값은 0 이상 10 미만입니다")
    elif 10 <= n < 20:
        print("입력한 값은 10 이상 20 미만입니다.")
    else:
        print("입력한 값은 20 이상 입니다.")

def check_phone_number():
    st = input("핸드폰 번호를 입력하세요 : ")
    if st.isdigit() and st.startswith("010") :
        print("정상 적으로 입력했습니다.")
    else :
        print("잘못된 번호 입니다.")


def get_multiple_val(n):
    if n.isdigit():
        print(int(n) ** 2)
    else:
        print("정수가 아닙니다.")