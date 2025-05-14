#코딩 기초 트레이닝
# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
def solution(myString, pat):
    answer = ""
    for i in range(len(myString) +1):
        sub = myString[:i]
        if sub.endswith(pat):
            answer = sub
    return answer
