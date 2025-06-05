#유형별 문제 풀이 - DP
# 피보나치 수열
"""
기존 피보나치 수열을 완전탐색(재귀)를 이용해서 풀면 시간복잡도 O(2**n)이 발생
재귀를 이용하기 때문에 중복되는 함수호출이 계속 발생해 비효율을 야기하게 된다

-> 중복 하위 문제가 계속 발생하는 과정을 해결하기 위해서 DP를 이용
   시간 복잡도를 O(n)으로 획기적으로 줄일 수 있음
"""
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

##------------------------

memo = {}  # memorization, 값들을 저장해서 불필요하게 함수를 재호출하는 것을 방지
def fibo_top_down(n):  # Top-down 방식, 재귀와 memoization을 더한 방식
    if n == 1 or n== 2:
        return 1
    if n not in memo:
        memo[n] = fibo_top_down(n-1) + fibo_top_down(n-2)
    return memo[n]

def fibo_bottom_up(n):  #Bottom-up 방식, 반복문으로 작은 문제들을 차례로 해결해나가는 방식
    if n == 1 or n == 2:
        return 1
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]