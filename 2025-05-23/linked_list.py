#유형별 문제 풀이 - 링크드 리스트
# 링크드 리스트 작성해보기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#노드를 먼저 정의하기, 노드에는 데이터와 다음 주소를 담을 next가 있음
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
#노드간 연결 만들기
#head로 처음 노드에 접근
#add 메서드로 새로운 노드를 만들고 current로 노드간 연결 만들기
