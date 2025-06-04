#유형별 문제 풀이 - 그래프
# Keys and Rooms
def canVisitAllRooms(rooms):
    visited = set()
    def dfs(cur_v):
        visited.add(cur_v)
        for next_v in rooms[cur_v]:
            if next_v not in visited:
                dfs(next_v)
    dfs(0)
    if len(visited) == len(rooms):
        return True
    else:
        return False

rooms = [[1,3], [2,4], [0], [4], [], [3,4]]
print(canVisitAllRooms(rooms))