#유형별 문제 풀이 - DP
# Dynamic Programming
"""
크고 복잡한 문제를 더 작은 문제들로 나눈다. (subproblem - 하위 문제)

하위 문제를 해결하면서 **중복 계산되는 부분 문제가 존재**한다. (overlapping subproblems - 중복 하위 문제)
→ 이러한 중복을 피하기 위해 한 번 계산한 결과는 메모리에 저장한다. (memoization 또는 dp table)

이렇게 저장된 하위 문제의 결과를 조합하여 원래 문제의 최적 해를 구할 수 있다. (optimal substructure - 최적 부분 구조)

- Overlapping Subproblems (중복되는 하위 문제 존재)
- Optimal Substructure (하위 문제의 최적 해가 전체 문제의 최적 해를 구성함)

DP 구현 방식:
1. Top-down (재귀 + memoization)
2. Bottom-up (반복문 기반, 작은 문제부터 차례로 해결)
"""
