#코딩 기초 트레이닝
# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer