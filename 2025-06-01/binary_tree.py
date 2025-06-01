#유형별 문제 풀이 - 이진 트리
# 이진 트리 작성해보기
class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left_child = left
        self.right_child = right

class BinaryTree:
    def __init__(self):
        self.root = None

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)


#완전 이진 트리("모든 레벨이 완전히 채워져 있고, 마지막 레벨만 왼쪽부터 채워져 있는 이진 트리")
#완전 이진 트리의 시간복잡도는 O(logN)
