#코딩 기초 트레이닝
# 수열과 구간 쿼리
def solution(arr, queries):
    for q in queries:
        i , j = q
        if i < len(arr) and j < len(arr):
            arr[i], arr[j] = arr[j], arr[i]
    return arr
