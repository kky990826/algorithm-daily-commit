#유형별 문제 풀이 - 완전탐색
# two sum 문제를 반복을 이용해서 완전탐색 실시
def solution(nums, target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
"""
위의 예시처럼 반복문을 사용해서 풀 수 있지만 만약 더해야하는 숫자가 늘어나면 그만큼 반복문도 만들어줘야함
k개의 숫자를 더하면 k번 반복문을 돌아야함
이때 완전탐색의 재귀를 이용
"""
def solution_by_recursion(nums, target):
    def backtrack(start, curr):
        if len(curr) == 2 and sum(nums[i] for i in curr) == target:
            return curr
        for i in range(start, len(nums)):
            curr.append(i)
            ret = backtrack(i+1, curr)
            if ret:
                return ret
            curr.pop()
        return None
    return backtrack(0, [])