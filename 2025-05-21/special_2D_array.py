#코딩 기초 트레이닝
# 특별한 이차원 배열
def solution(n):
    answer = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        answer.append(row)
    return answer

