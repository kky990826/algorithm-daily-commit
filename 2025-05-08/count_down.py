#코딩 기초 트레이닝
# 카운트 다운
def solution(start_num, end_num):
    answer = []
    for i in range(end_num, start_num+1):
        answer.append(i)
    answer.reverse()
    return answer