#유형별 문제 풀이 - DFS 깊이 우선 탐색
# 이진 트리로 깊이 우선 - 중위 순회 작성해보기
# 접근은 재귀를 통해 접근을 하였으나 방문(결과 출력)은 전위, 중위, 후위로 나뉨

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)  # 왼쪽 서브트리를 먼저 순회
    print(root.value) # 현재 노드 방문 (왼쪽 다 순회 후에)
    inorder(root.right) # 오른쪽 서브트리 순회

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)

inorder(bt.root)