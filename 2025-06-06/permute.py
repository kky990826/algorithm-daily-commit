#유형별 문제 풀이 - 완전탐색
# 순열을 만들어서 완전탐색과 백트래킹 파악하기
ans = []

def permute(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:]) # curr가 재귀적으로 계속 바뀌기 때문에 그 시점의 상태를 보존하기 위해 복사해서 저장
            return
        for num in nums:
            if num not in curr:
                curr.append(num) # 결정
                backtrack(curr)  # 진입
                curr.pop()       # 복구
    backtrack([])
    return ans

"""
백트래킹의 핵심은 항상 다음과 같은 3단계로 구성
1. 결정 - 다음에 어떤 값을 사용할지 
2. 진입 - 재귀 호출로 다음 단계로 진입
3. 복구 - 이전 선택을 취소하고 되돌림(백트래킹)
"""