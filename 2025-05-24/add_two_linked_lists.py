#유형별 문제 풀이 - 링크드 리스트
# 두 링크드 리스트 합 계산
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

def get_linked_list_sum(linked_list_1, linked_list_2):
    def list_to_string(linked_list):
        digits = []
        cur = linked_list.head
        while cur is not None:
            digits.append(str(cur.data))
            cur = cur.next
        return ''.join(digits)
    num_1 = int(list_to_string(linked_list_1))
    num_2 = int(list_to_string(linked_list_2))
    return num_1 + num_2
