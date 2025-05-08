#코딩 기초 트레이닝
# 배열 만들기
def solution(n, k):
    answer = []
    for i in range(1, n+1):
        if i % k == 0:
            answer.append(i)
    return answer
