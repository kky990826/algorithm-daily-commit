#코딩 기초 트레이닝
# 문자열 바꿔서 찾기
def solution(myString, pat):
    new_string = myString.replace("A" , "#").replace("B" , "A").replace("#" , "B")
    if pat in new_string:
        return 1
    else:
        return 0
    