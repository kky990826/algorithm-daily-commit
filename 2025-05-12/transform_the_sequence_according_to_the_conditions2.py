#코딩 기초 트레이닝
# 조건에 맞게 수열 변환하기2
def solution(arr):
    x = 0
    while True:
        new_arr = []
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                var = int(arr[i] / 2)
                new_arr.append(var)
            elif arr[i] < 50 and arr[i] % 2 != 0:
                var = int(arr[i] * 2 + 1)
                new_arr.append(var)
            else:
                new_arr.append(arr[i])
        if new_arr == arr:
            return x
        arr = new_arr
        x += 1