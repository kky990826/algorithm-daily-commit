#유형별 문제 풀이 - 이진 트리
# Maximum Depth of Binary Tree
from collections import deque

def maxDepth(root): #BFS로 구현해보기
    max_depth = 0
    if root is None:
        return 0
    q = deque()
    q.append((root, 1))
    while q:
        cur_node, cur_depth = q.popleft()
        max_depth = max(max_depth, cur_depth)
        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth + 1))
    return max_depth

class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v

root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth(root))

def maxDepth2(root):  #DFS 후위순회로 구현해보기
    if root is None:
        return 0
    left_depth = maxDepth2(root.left)
    right_depth = maxDepth2(root.right)
    return max(left_depth, right_depth) + 1
print(maxDepth2(root))
