#유형별 문제 풀이 - linked list
# 링크드 리스트 끝에서 K번째 값 출력하기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def get_kth_node_from_last(self, k):
        cur = self.head
        length = 1
        while cur.next is not None:
            cur = cur.next
            length +=1
        end_length = length - k
        cur = self.head # 처음에 cur을 끝까지 이동시켰기 때문에 다시 처음부터 이동해야 끝에서 k번째 노드를 찾을 수 있음
        for _ in range(end_length):
            cur = cur.next
        return cur

linked_list = LinkedList()
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)
k = 2
node = linked_list.get_kth_node_from_last(k)
print(node.data)