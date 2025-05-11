#코딩 기초 트레이닝
# 홀수 vs 짝수
def solution(num_list):
    total1 = 0
    total2 = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
             total1 +=num_list[i]
        else:
            total2 +=num_list[i]
    return max(total1, total2)