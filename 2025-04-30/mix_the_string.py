#코딩 기초 트레이닝
# 문자열 섞기
def solution(str1, str2):
    new_str = []
    for i in range(len(str1)):
        new_str.append(str1[i])
        new_str.append(str2[i])
    return "".join(new_str)

print(solution("abc", "pqr"))
