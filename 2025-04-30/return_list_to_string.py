#코딩 기초 트레이닝
# 문자 리스트를 문자열로 반환하기
def solution(arr):
    answer = ""
    for i in range(len(arr)):
        answer+= str(arr[i])
    return answer
