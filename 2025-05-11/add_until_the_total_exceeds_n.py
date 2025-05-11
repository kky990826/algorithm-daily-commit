#코딩 기초 트레이닝
# n보다 커질 때까지 더하기
def solution(numbers, n):
    for i in range(len(numbers)):
        if sum(numbers[:i+1]) > n:
            return sum(numbers[:i+1])