#코딩 기초 트레이닝
# 조건에 맞게 수열 변환하기
def solution(arr, k):
    for i in range(len(arr)):
        if k % 2 == 0:
            arr[i] = arr[i] + k
        else:
            arr[i] = arr[i] * k
    return arr