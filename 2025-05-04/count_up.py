#코딩 기초 트레이닝
# 카운트 업
def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer
print(solution(1, 10))