#코딩 기초 트레이닝
# 문자 개수 세기
def solution(my_string):
    counts = [0] * 52
    for i in range(len(my_string)):
        if 'A' <= my_string[i] <= 'Z':
            counts[ord(my_string[i]) - ord('A')] += 1
        elif 'a' <= my_string[i] <= 'z':
            counts[ord(my_string[i]) - ord('a') + 26] += 1
    return counts