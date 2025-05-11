#코딩 기초 트레이닝
# 수열과 구간 쿼리
def solution(arr, queries):
    for s, e in queries:
        for i in range(s, e + 1):
            arr[i] += 1
    return arr