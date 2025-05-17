#코딩 기초 트레이닝
# 배열의 길이를 2의 거듭제곱으로 만들기
import math

def solution(arr):
    length = len(arr)
    if (length & (length - 1) == 0):
        return arr
    next_power = 2 ** math.ceil(math.log2(length))
    return arr + [0] * (next_power - length)