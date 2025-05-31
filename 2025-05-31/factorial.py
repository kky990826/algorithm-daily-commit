#유형별 문제 풀이 - recursive
# 팩토리얼
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n -1)
# 시간복잡도는 O(n), 함수 하나가 하나의 재귀를 불러온다. 함수 각각의 시간복잡도는 1
# 따라서 전체 시간복잡도는 O(n)
# 재귀의 시간복잡도 = 재귀 함수 호출 수 * (재귀 함수 하나당)시간복잡도