#유형별 문제 풀이 - heap
# heap 구현
class MaxHeap:
    def __init__(self):
        self.items= [None]
    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) -1
        while cur_index != 1: # 1인 경우에는 root Node라 더 비교할게 없음
            parent_index = cur_index //2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break
        return
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()
        cur_index = 1
        while cur_index <= len(self.items) -1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index
            if left_child_index <= len(self.items) -1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index
            if right_child_index <= len(self.items) -1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index
            if max_index == cur_index:
                break
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index
        return prev_max


max_Heap = MaxHeap()
max_Heap.insert(3)
max_Heap.insert(4)
print(max_Heap.items)


import heapq #파이썬 heapq 라이브러리를 이용

min_heap = [5,3,9,4,1,2,6]
heapq.heapify(min_heap) # 시간복잡도 O(N)
heapq.heappop(min_heap) # 시간복잡도 O(logN)
heapq.heappush(min_heap, 7)# 시간복잡도 O(logN)

max_heap = [-x for x in min_heap] # heapq는 내부적으로 최소 힙(min-heap)만 지원하도록 설계
heapq.heapify(max_heap) # 음수로 바꿔서 간접적으로 최대 힙처럼 동작
print(-heapq.heappop(max_heap))
