# 문제: Two Sum
# 접근 방법: 브루트포스 (완전 탐색)

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# 예제 테스트
print(two_sum([2, 7, 11, 15], 9))
