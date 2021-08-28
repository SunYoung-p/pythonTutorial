def FuncTutorial():
    print("1 + 2 + 3 + 4 + 5 = ", 1 + 2 + 3 + 4 + 5)
    print("Simple is best!")
    print("행복한 파이썬~")


def FuncPractice_1(name):
    print("전달하신 문자열은 ", name, " 입니다")
    print("전달하신 문자열은 ", name, " 입니다")
    print("전달하신 문자열은 ", name, " 입니다")


def FuncPractice_2(num):
    print("전달하신 숫자는 ", num, " 이고, 부호를 바꾸어서 ", -1 * num, " 으로 출력합니다")


def FuncPractice_3(n, m):
    print(n, "과 ", m, f" 의 평균값 : {(n + m) / 2 : .1f}")


def adder3(num):
    return num * -1


def avger3(n1, n2):
    n = n1 + n2
    return f"{n / 2 : .2f}"


def input_func1():
    str = eval((input("첫 번째 입력은 ? ")))  # eval() 함수는 전달 인자를 산술 연산이 가능한 수(Number)로 바꾼다. 실수 포함.
    print("첫 번째 입력 : ", str)  # 하지만, 전달 인자를 aver3() 등의 함수로 할 경우, 이걸 분석해서 실행하기 때문에
    # 프로그래머가 명령하지 않은 함수 호출이 이뤄질 수 있으므로 보안에 취약하다.
    str2 = eval(input("두 번째 입력은 ? "))  # input 함수는 입력값을 하나의 문자열로 반환한다
    print("두 번째 입력 : ", str2)
    print("두 입력의 합 : ", str + str2)

def func_for1():
    sum = 0
    for i in [1,3,5,7,9]:
        sum += i
    return sum

def func_for2():
    n = 1
    for i in [1,2,3,4,5,6,7,8,9,10]:
        n *= i
    return n

def func_for3():
    n = 7
    for i in [1,2,3,4,5,6,7,8,9]:
        print(n," * ", i, " = ", n*i)

def func_for4():
    n = 7
    for i in [9,8,7,6,5,4,3,2,1]:
        print(n, " * ", i, " = ", n * i)