#코딩 기초 트레이닝
# 수 조작하기2
def solution(numLog):
    result = ""
    for i in range(len(numLog)-1):
        diff = numLog[i+1] - numLog[i]
        if diff == 1:
            result += "w"
        elif diff == -1:
            result += "s"
        elif diff == 10:
            result += "d"
        elif diff == -10:
            result += "a"
    return result