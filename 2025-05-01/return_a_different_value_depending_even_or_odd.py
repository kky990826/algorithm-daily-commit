#코딩 기초 트레이닝
# 홀짝에 따라 다른 값 반환하기
def solution(n):
    sum = 0
    if n % 2 == 0:
        for i in range(1, n//2 + 1):
            sum += (2 * i) ** 2
    else:
        for i in range(1, n//2 + 2):
            sum += 2 * i - 1
    return sum
