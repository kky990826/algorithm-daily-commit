#코딩 기초 트레이닝
# 수 조작하기1
def solution(n, control):
    control_list = list(control)
    for i in control_list:
        if i == "w":
           n = n +1
        elif i == "s":
           n = n -1
        elif i == "a":
           n = n - 10
        elif i == "d":
           n = n + 10
    return n
print(solution(5, "wswsww"))