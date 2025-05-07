#코딩 기초 트레이닝
# 접두사인지 확인하기
def solution(my_string, is_prefix):
    answer = []
    for i in range(len(my_string)):
        sliced_string = my_string[:i+1]
        answer.append(sliced_string)
        answer.sort()
    if is_prefix in answer:
        return 1
    else:
        return 0