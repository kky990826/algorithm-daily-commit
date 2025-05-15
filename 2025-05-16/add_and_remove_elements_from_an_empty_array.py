#코딩 기초 트레이닝
# 빈 배열에 추가, 삭제하기
def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            answer += [arr[i]] * (arr[i] *2)
        else:
            answer = answer[:-arr[i]]
    return answer
