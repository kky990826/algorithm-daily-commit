#코딩 기초 트레이닝
# 등차수열 특정 항만 더하기
def solution(a, d, included):
    sum = 0
    for i in range(len(included)):
        answer = a + i * d
        if included[i]:
            sum += answer
    return sum
