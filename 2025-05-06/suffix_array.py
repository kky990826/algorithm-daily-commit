#코딩 기초 트레이닝
# 접미사 배열
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        sliced_string = my_string[i:]
        answer.append(sliced_string)
        answer.sort()
    return answer