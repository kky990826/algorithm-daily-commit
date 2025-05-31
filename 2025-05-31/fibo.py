#유형별 문제 풀이 - recursive
# 피보나치 수열
def fibo(n):
    if n ==1 or n==2:
        return 1
    return fibo(n -1)+ fibo(n -2)

# 시간복잡도는 O(2**n), 함수 하나가 두개의 재귀를 일으키기 때문, 함수 각각의 시간복잡도는 1
# 따라서 전체 시간복잡도는 O(2**n)