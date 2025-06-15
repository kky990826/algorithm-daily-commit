#유형별 문제 풀이 - BFS
# 로봇 청소기가 청소한 부서 개수 반환

from collections import deque

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_d_index_when_rotate_to_left(d):
    return (d+3) % 4

def get_d_index_when_go_back(d):
    return (d+2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_department_cleaned = 1
    room_map[r][c] = 2
    queue = deque([(r,c,d)])
    while queue:
        r,c,d = queue.popleft()
        temp_d = d
        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_department_cleaned +=1
                room_map[new_r][new_c] = 2
                queue.append((new_r, new_c, temp_d))
                break
            elif i == 3:
                temp_d = get_d_index_when_go_back(d)
                new_r, new_c = r + dr[temp_d], c + dc[temp_d]
                queue.append((new_r, new_c, d))
                if room_map[new_r][new_c] == 1:
                    return count_of_department_cleaned

    return count_of_department_cleaned
