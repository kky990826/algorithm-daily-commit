#코딩 기초 트레이닝
# 주사위 게임
from collections import Counter

def solution(a, b, c, d):
    count = Counter([a, b, c, d])
    nums = list(count.keys())
    freqs = list(count.values())

    if len(count) == 1:
        return 1111 * nums[0]

    elif len(count) == 2:
        if 3 in freqs:
            p = nums[freqs.index(3)]
            q = nums[freqs.index(1)]
            return (10 * p + q) ** 2
        else:
            return (nums[0] + nums[1]) * abs(nums[0] - nums[1])

    elif len(count) == 3:
        single_nums = [n for n in nums if count[n] == 1]
        return single_nums[0] * single_nums[1]

    else:
        return min(a, b, c, d)
