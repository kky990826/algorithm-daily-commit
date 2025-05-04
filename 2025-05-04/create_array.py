#코딩 기초 트레이닝
# 배열 만들기
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(ch in {"0", "5"} for ch in str(i)):
            answer.append(i)
        else:
            continue
    return answer or [-1]