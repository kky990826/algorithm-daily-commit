#코딩 기초 트레이닝
# 배열 조각하기
def solution(arr, query):
    for i in range(len(query)):
        q = query[i]
        if q >= len(arr):
            q = len(arr) - 1
        if i % 2 == 0:
            arr = arr[:q+1]
        else:
            arr = arr[q:]
    return arr