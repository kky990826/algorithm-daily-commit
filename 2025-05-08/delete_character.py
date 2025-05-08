#코딩 기초 트레이닝
# 글자 지우기
def solution(my_string, indices):
    my_list = list(my_string)
    for idx in indices:
        my_list[idx] = ''
    return ''.join(my_list)