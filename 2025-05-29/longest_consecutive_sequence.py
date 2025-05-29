#유형별 문제 풀이 - dict
# 가장 긴 연속된 수열
def longest_consecutive_sequence(nums):  # dict을 사용해서 시간복잡도 O(N)으로 풀이
    longest = 0
    nums_dict = {}
    for i in nums:  # dict에 모든 원소 저장 O(N)
        nums_dict[i] = 1
    for i in nums_dict: # 각 원소에 대해서 한번씩 O(N)
        if i -1 not in nums_dict:
            count = 1
            target = i + 1
            while target in nums_dict:  # while 루프에서 각 숫자는 최대 1번만 target in nums_dict로 검사됨
                count+=1
                target +=1
            longest = max(longest, count)
    return longest

def longest_consecutive_sequence2(nums): # 정렬 알고리즘을 사용해서 시간복잡도 O(NlogN)으로 풀이
    if not nums:
        return 0
    nums.sort()
    longest = 1
    current_streak = 1
    for i in range(1, len(nums)): # 1번째 index부터 시작해야 0번째 index 상황에서 -1번째 index와 비교하지 않음
        if nums[i] == nums[i -1]: # 지금 index와 이전 index가 서로 같은 상황
            continue
        elif nums[i] == nums[i -1] + 1:
            current_streak +=1
        else:
            longest = max(longest, current_streak) # 수열이 끊겼을때, longest를 저장
            current_streak = 1
    return max(longest, current_streak)
