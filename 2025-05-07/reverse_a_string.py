#코딩 기초 트레이닝
# 문자열 뒤집기
def solution(my_string, s, e):
    reversed_string = my_string[:s]+ my_string[s:e+1][::-1] + my_string[e+1:]
    return reversed_string
