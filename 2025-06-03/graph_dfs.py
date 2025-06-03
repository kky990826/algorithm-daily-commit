#유형별 문제 풀이 - 그래프
# DFS 구현하기
graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}

def dfs(graph, cur_v, visited=None):
    if visited is None:
        visited = []
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(graph, v, visited)
    return visited
print(dfs(graph, "A"))

#스택을 이용해서 풀어보기
# 1. 시작 노드를 스택에 넣기
# 2. 현태 스택의 노드를 빼서 visited에 추가
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가
# 위 과정을 스택이 빌때까지 반복
def dfs_stack(graph, cur_v):
    stack = [cur_v]
    visited = []
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            for v in graph[current_node]:
                stack.append(v)
    return visited
print(dfs_stack(graph, "A"))