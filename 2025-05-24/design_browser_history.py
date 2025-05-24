#유형별 문제 풀이 - 링크드 리스트
# Design Browser History
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.head
    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = self.current.next
        return None
    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev != None:
            self.current = self.current.prev
            steps -= 1
        return self.current.data
    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next != None:
            self.current = self.current.next
            steps -= 1
        return self.current.data