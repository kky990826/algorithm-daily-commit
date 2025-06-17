#유형별 문제 풀이 - DP
# N으로 표현

def solution(N, number):
    if N == number:  # N 하나만으로 이미 number를 만들 수 있으면 바로 return
        return 1

    dp = [set() for _ in range(9)]  # dp[i]는 N을 i번 사용해서 만들 수 있는 수들의 집합, 1부터 8까지 생성, 5, 55, 555,555

    for i in range(1, 9): # N을 1번부터 8번까지 사용하는 경우를 순회
        dp[i].add(int(str(N) * i))  # N을 i번 이어붙여서 만든 수를 먼저 dp[i]에 추가

        for j in range(1, i): #dp[i]를 만들기 위해, 더 작은 조각들의 조합을 생각
            for op1 in dp[j]:
                for op2 in dp[i - j]:  #dp[j]에 있는 수와 dp[i-j]에 있는 수를 서로 연산해서 dp[i]에 가능한 수를 추가
                    dp[i].add(op1 + op2) #기본적인 덧셈, 뺄셈, 곱셈 결과를 dp[i]에 추가
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0: #나눗셈은 op2가 0일 경우를 피해서 정수 나눗셈 결과만 추가
                        dp[i].add(op1 // op2)

        if number in dp[i]: #현재 dp[i] 안에 우리가 찾는 number가 있다면, 바로 i를 반환
            return i

    return -1  # 8번까지 해도 안 되면 -1