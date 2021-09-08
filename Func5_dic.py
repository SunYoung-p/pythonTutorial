def dic_exam_1():
    dic = {'새우깡': 900, '콘치즈': 850, '꼬깔콘': 750}
    print(dic)
    dic['홈런볼'] = 900  # 딕셔너리에 새 값 추가
    print(dic)

    for i in dic:
        dic[i] += 100  # i에는 key 값이 들어감
    print(dic)

    del dic['콘치즈']
    dic['치즈콘'] = 950
    print(dic)