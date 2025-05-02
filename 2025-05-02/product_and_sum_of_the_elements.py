#코딩 기초 트레이닝
# 원소들의 곱과 합
def solution(num_list):
    sum1 = 1
    sum2 = 0
    for i in range(len(num_list)):
        sum1 *= num_list[i]
        sum2 += num_list[i]
    return 0 if sum1 > sum2 ** 2 else 1
