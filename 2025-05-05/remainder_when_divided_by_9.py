#코딩 기초 트레이닝
# 9로 나눈 나머지
def solution(number):
    sum = 0
    for i in number:
        sum+=int(i)
    answer = sum % 9
    return answer