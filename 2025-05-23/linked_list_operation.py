#유형별 문제 풀이 - 링크드 리스트
# 링크드 리스트 operation 만들기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    #====get 메서드 만들기====
    def get(self, index):
        current = self.head
        for i in range(index):
            if current.next is None:
                return "IndexError: list index out of range"
            current = current.next
        return current.data #index만큼 이동해서 data 추출
    #====insert 메서드 만들기====
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:  #index가 0인 상황, 즉 맨 앞에 새로운 노드를 만들때임
            new_node.next = self.head #현재 노드는 새로운 노드 다음임을 명시
            self.head = new_node #새로운 노드에 head를 지정
        else:
            current = self.head  #index가 0이 아닌 상황에서는 current를 사용해서 이동
            for i in range(index - 1):
                if current.next is None: #리스트 길이보다 더 큰 index를 삽입하려고 할때
                    return "IndexError: list index out of range"
                current = current.next #current 이동
            new_node.next = current.next #먼저 새로운 노드와 다음 노드를 연결
            current.next = new_node # 새로운 노드와 이전 노드를 연결
    #====remove 메서드 만들기====
    def remove(self, index):
        if index == 0: #index가 0인 상황, 즉 맨 앞에 노드를 삭제할때임
            self.head = self.head.next #현재 노드의 다음 노드에 head를 지정
        else:
            current = self.head
            for i in range(index - 1):
                if current.next is None: #리스트 길이보다 더 큰 index를 삭제하려고 할때
                    return "IndexError: list index out of range"
                current = current.next #current 이동
            current.next = current.next.next #현재 노드가 다음 다음 노드를 가리킴