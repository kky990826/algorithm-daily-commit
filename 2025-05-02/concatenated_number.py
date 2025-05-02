#코딩 기초 트레이닝
# 이어붙인 수
def solution(num_list):
    odd_str = ""
    even_str = ""
    for i in num_list:
        if i % 2 == 0:
            even_str += str(i)
        else:
            odd_str += str(i)
    return int(odd_str) + int(even_str)