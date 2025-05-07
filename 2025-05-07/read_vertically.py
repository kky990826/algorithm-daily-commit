#코딩 기초 트레이닝
# 세로 읽기
def solution(my_string, m, c):
    answer = ''
    for i in range(0, len(my_string), m):
        answer += my_string[i + c - 1]
    return answer