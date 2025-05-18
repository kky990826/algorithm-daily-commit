#코딩 기초 트레이닝
# 문자열 정수의 합
def solution(num_str):
    num_str = list(num_str)
    num_str = sum(map(int, num_str))
    return num_str