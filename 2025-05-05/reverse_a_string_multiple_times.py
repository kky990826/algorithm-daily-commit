#코딩 기초 트레이닝
# 문자열 여러번 뒤집기
def solution(my_string, queries):
    my_list = list(my_string)
    for i in queries:
        my_list[i[0]:i[1]+1] = my_list[i[0]:i[1]+1][::-1]
    new_string = ''.join(my_list)
    return new_string