#유형별 문제 풀이 - 완전탐색
# 조합을 만들어서 완전탐색과 백트래킹 파악하기

def combination(nums, k): # nums가 주어졌을때 k개의 원소로 이루어진 모든 조합을 구하기
    result = []

    def backtracking(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()
    backtracking(0, [])
    return result

# k가 변하는 것을 이용하면 부분집합도 구할 수 있음
def combination_subset(nums):
    result = []

    def backtracking(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()
    for k in range(len(nums) +1):
        backtracking(0, [])
    return result
