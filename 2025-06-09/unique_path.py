#유형별 문제 풀이 - DP
# Unique Path
def dfs(r,c):
    if r == 0 and c == 0:
        return 1
    unique_paths = 0
    if r-1 >=0:
        unique_paths += dfs(r-1, c)
    if c-1 >=0:
        unique_paths += dfs(r, c-1)
    return unique_paths

# DP 방식으로 구현
memo = {}
def dfs_by_dp(r, c):
    if r == 0 and c == 0:
        memo[(r,c)] = 1
        return memo[(r,c)]
    unique_paths = 0
    if (r,c) not in memo:
        if r-1>=0:
            unique_paths += dfs_by_dp(r-1, c)
        if c-1>=0:
            unique_paths += dfs_by_dp(r, c-1)
        memo[(r,c)] = unique_paths
    return memo[(r,c)]
