#코딩 기초 트레이닝
# 배열에서 문자열 대소문자로 변환하기
def solution(strArr):
    new_strArr = []
    for idx, i in enumerate(strArr):
        if idx % 2 == 0:
            new_strArr.append(i.lower())
        else:
            new_strArr.append(i.upper())
    return new_strArr