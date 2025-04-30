#코딩 기초 트레이닝
# 더 크게 합치기
def solution(a, b):
    num1 = str(a)
    num2 = str(b)
    if num1 + num2 >= num2 + num1:
        return int(num1 + num2)
    else:
        return int(num2 + num1)