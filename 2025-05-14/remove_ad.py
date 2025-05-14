#코딩 기초 트레이닝
# ad 제거하기
def solution(strArr):
    newArr = []
    for i in strArr:
        if 'ad' in i:
            continue
        else:
            newArr.append(i)
    return newArr