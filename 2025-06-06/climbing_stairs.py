#유형별 문제 풀이 - DP
# 계단 오르기
memo = {}
def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = cs(n-1) + cs(n-2)
    return memo[n]


def cs2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]
