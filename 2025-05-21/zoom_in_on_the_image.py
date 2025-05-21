#코딩 기초 트레이닝
# 그림 확대
def solution(picture, k):
    result = []
    for i in picture:
        expanded = ''
        for j in i:
            expanded += j * k
        for _ in range(k):
            result.append(expanded)
    return result