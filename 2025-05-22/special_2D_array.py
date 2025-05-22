#코딩 기초 트레이닝
# 특별한 이차원 배열
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1
