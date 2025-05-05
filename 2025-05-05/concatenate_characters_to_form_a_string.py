#코딩 기초 트레이닝
# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    new_string = ''
    for i in range(len(index_list)):
        var = my_string[index_list[i]]
        new_string += var
    return new_string