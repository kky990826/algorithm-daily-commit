#코딩 기초 트레이닝
# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    for i in range(len(arr)):
        if len(arr) % 2 == 0:
            if i % 2 != 0:
                arr[i] += n
        else:
            if i % 2 == 0:
                arr[i] += n
    return arr