#유형별 문제 풀이 - 리스트
# 두 원소를 더해서 합
"""
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False
"""
# 위 방법은 시간 복잡도 O(n**2)의 방법, 제약 조건 2 <= nums.length <= 10**4
# for문을 2번 돌리는 것보다 좀 더 효율적인 방법 필요
def twoSum(nums, target):
    nums.sort()
    l , r = 0, len(nums)-1
    while l < r:
        if nums[l] + nums[r] == target:
            return True
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    return False