#유형별 문제 풀이 - DFS 깊이 우선 탐색
# 이진 트리로 깊이 우선 - 후위 순회 작성해보기
# 접근은 재귀를 통해 접근을 하였으나 방문(결과 출력)은 전위, 중위, 후위로 나뉨

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

def postorder(root):
    if root is None:
        return
    postorder(root.left)  # 왼쪽 서브트리를 먼저 순회 (재귀 호출)
    postorder(root.right)  # 그다음 오른쪽 서브트리를 순회 (재귀 호출)
    print(root.value)  # 모든 자식 노드를 방문한 후 현재 노드 처리

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)

postorder(bt.root)