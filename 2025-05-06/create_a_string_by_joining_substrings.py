#코딩 기초 트레이닝
# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for idx in range(len(parts)):
        start, end = parts[idx]
        answer += my_strings[idx][start:end+1]
    return answer
