#유형별 문제 풀이 - dfs
# 타겟 넘버

def solution(numbers, target):
    result_count = 0

    def dfs(index, total):
        nonlocal result_count
        if index == len(numbers):
            if total == target:
                result_count +=1
            return
        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])
    dfs(0,0)
    return result_count
