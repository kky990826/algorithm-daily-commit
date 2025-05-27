#유형별 문제 풀이 - 스택
# 탑 높이에 따라 레이저 수신
def get_receiver_top_orders(heights):
    n = len(heights)
    top_height = [0] * n
    stack = []
    for i in range(n - 1, -1, -1):  # 오른쪽에서 왼쪽으로 탐색
        while stack and heights[i] > heights[stack[-1]]:
            idx = stack.pop()
            top_height[idx] = i + 1  # 탑 번호는 1-based
        stack.append(i)
    return top_height