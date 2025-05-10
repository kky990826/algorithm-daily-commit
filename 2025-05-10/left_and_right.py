#코딩 기초 트레이닝
# 왼쪽 오른쪽
def solution(str_list):
    for i, s in enumerate(str_list):
        if s == "l":
            return str_list[:i]
        elif s == "r":
            return str_list[i+1:]
    return []