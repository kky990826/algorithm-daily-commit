#코딩 기초 트레이닝
# 주사위 게임
def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        return a**2 + b**2
    elif a % 2 == 0 and b % 2 == 0:
        return abs(a - b)
    else:
        return 2 * (a + b)