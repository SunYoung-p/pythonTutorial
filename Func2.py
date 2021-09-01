# List and String
def list_basic():
    st = [1, 2, 3, 4]
    print(st[0], st[1], st[2], st[3])
    print(st[0], st[-3], st[-2], st[-1])

    st[0] += 1
    st[1] += 1
    st[2] += 1
    st[3] += 1
    print(st)

    st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(st)
    for i in range(0, 10):
        st[i] += 1
    print(st)

    st = [1, 2, 3, 4, 5, 6]
    print(st)
    st[0], st[5] = st[5], st[0]
    print(st)
    st[0:7] = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 슬라이싱 연산에 의한 리스트 값 수정 시, 수정할 값의 개수가 많고 적음은 상관없이 실행된다.
    print(st)


def idx_list():
    st = [1, 2, 3, 4, 5]
    print(st)
    st[1:4] = [3]
    print(st)
    st = [1, 2, 3, 4, 5]
    print(st)
    st[2:4] = [3, 3.5, 4]
    print(st)
    st = [1, 2, 3, 4, 5]
    print(st)
    st[1:4] = []
    print(st)
    st = [1, 2, 3, 4, 5]
    print(st)
    st = []
    print(st)
    st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(st)
    nt = st[::2]
    print(nt)
    st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(st)
    nt = st[1::2]
    print(nt)


def idx_string():
    str = "Hello"
    print(str)
    str = str + "World"
    print(str)

    str = "Hello"
    print(str)
    str += "World"
    print(str)
    print(str[:3])


def sum_all(li):
    sum = 0
    for i in li:
        sum += i
    return sum


def show_reverse(li):
    leng = len(li)
    for i in li:  # range(li) 는 잘못된 표현. range 가 list를 리턴해주는 것 같다
        print(li[leng - 1], end=' ')
        leng -= 1


def apend_pop_list():
    st = []
    print(st)
    st.append(1)
    st.append(2)
    st.append(3)
    print(st)
    st.pop(0)
    st.pop(0)
    st.pop(0)
    print(st)


def apend_pop_list2():
    st = []
    print(st)
    st.append(1)
    st.append(2)
    st.append(3)
    print(st)
    st.pop(-1)
    st.pop(-1)
    st.pop(-1)  # list 에 원소가 1개만 있을 경우, idx값 0 == -1 이다
    print(st)


def clear_list():
    st = [1, 2, 3, 4]
    print(st)
    st[:] = []  # st.clear()
    print(st)


def for_list_01():
    st = []
    print(st)
    for i in range(10):
        st.append(i + 1)
    print(st)
    for i in range(10):
        st.pop(0)
    print(st)


def for_list_02():
    st = []
    print(st)
    for i in range(10):
        st.append(i + 1)
    print(st)
    for i in range(10):
        st.pop(-1)
    print(st)


def slice_li():
    st = [1, 2]
    print(st)
    st[100:] = [3, 4, 5]  # st.extend([3,4,5]) - 슬라이싱 연산에서는 인덱스 값이 배열 크기보다 커도 상관 없다
    print(st)


def str_func_2():
    str = "The Espresso Spirit"
    print(str.upper())
    print(str.lower())
    print(str)


def birth_only(st):
    str = ""
    str += st
    return str.split('-')[0]

"""
문자열 서치 관련.
str.find(sub) - str에 담긴 문자열 안에 sub가 있는 위치의 idx 반환. sub가 없으면 -1 반환
str.rfind(sub) - find랑 똑같은데 뒤에서부터 idx를 카운트함
sub in str - sub가 포함됬으면 true, 아니면 false ==> list에도 쓸 수 있다.
sub not in str - in 의 반대
"""
