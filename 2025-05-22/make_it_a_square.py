#코딩 기초 트레이닝
# 정사각형으로 만들기
def solution(arr):
    row = len(arr)
    col = len(arr[0]) if row else 0
    max_len = max(row, col)
    for i in range(row):
        arr[i] += [0] * (max_len - len(arr[i]))
    for _ in range(max_len - row):
        arr.append([0] * max_len)
    return arr