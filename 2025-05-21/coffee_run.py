#코딩 기초 트레이닝
# 커피 심부름
def solution(order):
    total_ordering = 0
    for i in range(len(order)):
        if "americano" in order[i] or "anything" in order[i]:
            total_ordering += 4500
        else:
            total_ordering += 5000
    return total_ordering