#코딩 기초 트레이닝
# 공배수
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0