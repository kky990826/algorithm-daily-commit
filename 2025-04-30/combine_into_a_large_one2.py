#코딩 기초 트레이닝
# 두 수의 연산값 비교하기
def solution(a, b):
    num1 = str(a) + str(b)
    mult = 2 * a * b
    return max(mult, int(num1))
