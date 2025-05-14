#코딩 기초 트레이닝
# 문자열이 몇 번 등장하는지 세기
def solution(myString, pat):
    count = 0
    for i in range(len(myString)):
        if myString[i:i+len(pat)] == pat:
            count += 1
    return count
