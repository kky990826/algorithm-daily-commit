#유형별 문제 풀이 - 큐
# 주식 가격
from collections import deque

def get_price_not_fall_periods(prices):
    result = []
    queue = deque(prices)
    while queue:
        price_not_fall_periods = 0
        current_price = queue.popleft()
        for next_price in queue:
            if current_price > next_price:
                price_not_fall_periods += 1
                break
            else:
                price_not_fall_periods += 1
        result.append(price_not_fall_periods)
    return result