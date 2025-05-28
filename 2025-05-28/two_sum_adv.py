#유형별 문제 풀이 - dict
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
'''def twoSum(nums, target):
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
'''
# 정렬 알고리즘을 사용, two pointer를 이용해 시간 복잡도 O(NlogN)으로 문제를 풀었었다
# 이제 더 나아가 dict을 활용해서 문제를 더 효율적으로 풀어보기
def twoSum(nums, target):
    s = {}
    for i in nums:
        s[i] = 1 # 여기서는 value 값이 중요하지 않고 key 값이 중요
    for i in nums:
        needed_number = target - i
        if needed_number in s:
            return True
    return False
# 하나의 원소를 중복해서 더해 target을 구하는 오류가 있음

def twoSum2(nums, target):
    s = {}
    for i, num in enumerate(nums): #enumerate 사용, list안에 튜플 생성
        needed_number = target - num
        if needed_number in s:
            return True
        s[num] = i # 원래는 idx : value 구조의 enumerate 생성해야하나 여기선 value : idx 구조
    return False