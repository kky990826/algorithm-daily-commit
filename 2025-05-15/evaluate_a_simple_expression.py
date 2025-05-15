#코딩 기초 트레이닝
# 간단한 식 계산하기
def solution(binomial):
    a, op, b = binomial.split()
    return eval(f'{a}{op}{b}')
