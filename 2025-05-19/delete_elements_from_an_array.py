#코딩 기초 트레이닝
# 배열의 원소 삭제하기
def solution(arr, delete_list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr