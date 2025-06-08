#유형별 문제 풀이 - 다익스트라 알고리즘
# 다익스트라 구현
"""
그래프에서 한 정점(시작점)으로부터 다른 모든 정점까지의 최단 경로를 찾는 알고리즘

비가중치일때는 BFS가 최단 경로를 찾아줌 - 너비 우선 탐색이기 때문에 시작점에서부터 가장 적은 간선을 거친 노드를 방문
처음 방문한 경로가 곧 가장 짧은 경로가 되기 때문에 BFS가 최단 경로

가중치일때는 다익스트라 알고리즘이 최단 경로를 찾아줌 - 우선순위 큐를 사용해서 효율적으로 처리
방문할 수 있는 노드중에 가장 비용이 작은 곳 방문(우선순위가 높은 곳)



다익스트라 알고리즘 동작
1. 우선 순위큐에 시작노드 추가
2. 우선순위가 가장 높은 노드 추출
3. 방문 여부 확인
4. 비용 업데이트
5. 현재 노드와 연결된 노드 우선순위 큐에 추가 (2~5번 과정 반복)
6. 목적지에 기록된 비용 반환

다익스트라 알고리즘은 우선순위 큐에다 엣지의 개수만큼 삽입하고 삭제를 하므로 O(ElogE)의 시간복잡도
"""
import heapq

graph = {
    1: [(2,2), (1,4)],
    2: [(1,3), (9,5), (6,6)],
    3: [(4,6)],
    4: [(3,3), (5,7)],
    5: [(1,8)],
    6: [(3,5)],
    7: [(7,6), (9,8)],
    8: []
}  # (i,j) -> i가 가중치, j는 노드

def dijkstra(graph, start, final):
    costs = {}
    pq = []
    heapq.heappush((pq, (0, start)))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))
    return costs[final]
