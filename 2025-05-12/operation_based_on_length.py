#코딩 기초 트레이닝
# 길이에 따른 연산
def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        answer = 1
        for num in num_list:
            answer *= num
    return answer