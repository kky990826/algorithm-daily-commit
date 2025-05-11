#코딩 기초 트레이닝
# 할일 목록
def solution(todo_list, finished):
    result = []
    for i in range(len(finished)):
        if not finished[i]:
            result.append(todo_list[i])
    return result
