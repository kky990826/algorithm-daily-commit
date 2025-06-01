#유형별 문제 풀이 - DFS 깊이 우선 탐색
# 이진 트리로 깊이 우선 - 전위 순회 작성해보기
# 접근은 재귀를 통해 접근을 하였으나 방문(결과 출력)은 전위, 중위, 후위로 나뉨

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

def preorder(root):
    if root is None:
        return
    print(root.value) # 먼저 현재 노드를 방문하고 다음 노드로 들어가기
    preorder(root.left)  # 재귀를 이용
    preorder(root.right) # 재귀를 이용

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)

preorder(bt.root)