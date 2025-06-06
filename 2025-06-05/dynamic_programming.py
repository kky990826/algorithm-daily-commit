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
"""
문제 적용시 
1. Optimum value(최대, 최소), 방법의 개수 등을 구할 때
- ~의 최소 비용은?
- ~의 최대 이익은?
- ~를 하는 방법의 개수는?
- What is the longest possible...
- 특정 지점에 도달할 수 있는지?

2. 미래의 계산이 앞선 계산 결과에 영향을 받을 때

이런 유형은 DP를 적용하는 것을 고려!
"""