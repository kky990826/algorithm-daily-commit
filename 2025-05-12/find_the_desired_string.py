#코딩 기초 트레이닝
# 원하는 문자열 찾기
def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    if pat in myString:
        return 1
    else:
        return 0