#코딩 기초 트레이닝
# 조건에 맞게 수열 변환하기
def solution(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            var = int(arr[i] / 2)
            new_arr.append(var)
        elif arr[i] < 50 and arr[i] % 2 != 0:
            var = int(arr[i] * 2)
            new_arr.append(var)
        else:
            new_arr.append(arr[i])
    return new_arr
