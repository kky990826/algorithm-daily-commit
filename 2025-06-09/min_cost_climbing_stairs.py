#유형별 문제 풀이 - DP
# Min cost Climbing Stairs
cost = [10,15,20,17,1]
def dfs(n):
    if n == 0 or n == 1:
        return 0
    return min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
# 시간복잡도가 너무 큼 O(2**n)

def dp_top_down(n):
    memo = {}
    if n == 0 or n ==1:
        return 0
    if n not in memo:
        memo[n] = min(dp_top_down(n-1) + cost[n-1], dp_top_down(n-2) + cost[n-2])
    return memo[n]

def dp_bottom_up(n):
    memo2 = [0] * (n + 1)
    for i in range(2, n + 1):
        memo2[i] = min(memo2[i-1] + cost[i-1], memo2[i-2] + cost[i-2])
    return memo2[n]
