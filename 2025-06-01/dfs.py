#유형별 문제 풀이 - DFS 깊이 우선 탐색
# 이진 트리로 깊이 우선 작성해보기

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

def dfs(root):
    if root is None:
        return
    dfs(root.left)  # 재귀를 이용
    dfs(root.right) # 재귀를 이용

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)