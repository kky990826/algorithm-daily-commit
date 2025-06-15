#유형별 문제 풀이 - heap
# 해외에서 보급을 최소 몇 번 받아야 하는지 구하기
import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []

    while stock <= k:
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock :
            heapq.heappush(max_heap, supplies[last_added_date_index] * -1)
            last_added_date_index +=1
        supply = heapq.heappop(max_heap) * -1
        stock += supply
        answer +=1
    return answer

