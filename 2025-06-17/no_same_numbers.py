#유형별 문제 풀이 - 리스트
# 같은 숫자는 싫어

def solution(arr):
    answer = []
    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)
    return answer