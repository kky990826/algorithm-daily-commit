#코딩 기초 트레이닝
# 2의 영역
def solution(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] == 2:
            new_arr.append(i)
    if not new_arr:
        return [-1]
    return arr[new_arr[0]: new_arr[-1]+1]

