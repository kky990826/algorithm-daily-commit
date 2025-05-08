#코딩 기초 트레이닝
# 가까운 1 찾기
def solution(arr, idx):
    for i in range(len(arr)):
        if arr[i] == 1 and i >= idx:
            return i
    return -1
