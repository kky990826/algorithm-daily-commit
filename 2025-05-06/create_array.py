#코딩 기초 트레이닝
# 배열 만들기
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        slice = i[s:s+l]
        if int(slice) > k:
            answer.append(int(slice))
    return answer