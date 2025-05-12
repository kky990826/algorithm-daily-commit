#코딩 기초 트레이닝
# 1로 만들기
def solution(num_list):
    total_count = 0
    for i in num_list:
        while i != 1:
            total_count += 1
            if i % 2 == 0:
                i = i / 2
            else:
                i =(i -1) / 2
    return total_count