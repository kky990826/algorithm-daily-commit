#코딩 기초 트레이닝
# 첫 번째로 나오는 음수
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1