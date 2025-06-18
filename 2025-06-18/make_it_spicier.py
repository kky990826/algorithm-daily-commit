#유형별 문제 풀이 - 힙
# 모든 음식의 스코빌 지수를 K 이상으로 만들기
import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville) # 리턴값이 None, 리스트를 직접 변경할 뿐 아무것도 반환하지 않는다.
    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_food = first + second *2
        heapq.heappush(scoville, new_food)
        count +=1
    return count if scoville[0] >= K else -1

# 힙을 쓸때는 인덱스로 일일이 접근하거나 pop()으로 빼면 힙 성질이 깨질 수 있음
