#코딩 기초 트레이닝
# 주사위 게임
def solution(a, b, c):
    sum = 0
    if a != b and b != c and a != c:
        sum = a + b + c
    elif a == b and b == c:
        sum = (a + b + c) * ( a**2 + b**2 + c**2 ) * (a**3 + b**3 + c**3)
    elif a == b or b == c or a == c:
        sum =  (a + b + c) * (a**2 + b**2 + c**2)
    return sum