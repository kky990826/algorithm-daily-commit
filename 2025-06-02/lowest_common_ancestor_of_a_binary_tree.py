#유형별 문제 풀이 - 이진 트리
# LCA 찾기
from collections import deque  # 큐를 사용하기 위해 import (레벨 순회에 사용)

# 트리 노드 클래스 정의
class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value      # 노드의 값 저장
        self.left = left        # 왼쪽 자식 노드
        self.right = right      # 오른쪽 자식 노드

# 리스트를 이진 트리로 변환 (None 포함 리스트 처리 가능)
def build_tree_with_none(values):
    if not values or values[0] is None:
        return None  # 빈 리스트거나 첫 값이 None이면 트리 없음

    root = Node(values[0])     # 루트 노드 생성
    queue = deque([root])      # 레벨 순회를 위한 큐
    i = 1                      # 리스트에서 현재 처리할 인덱스

    while queue and i < len(values):  # 큐가 비지 않고, 리스트 끝나지 않았을 때
        current = queue.popleft()     # 현재 부모 노드 꺼냄

        # 왼쪽 자식 처리
        if i < len(values) and values[i] is not None:
            current.left = Node(values[i])  # 왼쪽 자식 노드 생성
            queue.append(current.left)      # 큐에 추가하여 다음 자식들 연결 예정
        i += 1  # 다음 인덱스로 이동

        # 오른쪽 자식 처리
        if i < len(values) and values[i] is not None:
            current.right = Node(values[i])  # 오른쪽 자식 노드 생성
            queue.append(current.right)      # 큐에 추가
        i += 1  # 다음 인덱스로 이동

    return root  # 트리의 루트 노드 반환

# 특정 값에 해당하는 노드 찾기 (DFS 방식)
def find_node(root, target_value):
    if root is None:
        return None  # 노드가 없으면 종료
    if root.value == target_value:
        return root  # 찾았으면 반환
    left = find_node(root.left, target_value)  # 왼쪽 서브트리 탐색
    if left:
        return left
    return find_node(root.right, target_value)  # 오른쪽 서브트리 탐색

# LCA (최소 공통 조상) 찾기
def LCA(root, p, q):
    if root is None:
        return None  # 트리가 비었으면 None 반환
    if root == p or root == q:
        return root  # 자기 자신이 p 또는 q이면 그 노드 반환
    left = LCA(root.left, p, q)   # 왼쪽 서브트리에서 LCA 탐색
    right = LCA(root.right, p, q) # 오른쪽 서브트리에서 LCA 탐색

    if left and right:
        return root  # 양쪽에서 하나씩 찾았으면 현재 노드가 LCA
    return left or right  # 둘 중 하나만 존재하면 그 노드가 LCA

# ---------- 실행 파트 ----------

tree_values = [3,5,1,6,2,0,8,None,None,7,4]  # 주어진 트리 리스트
root = build_tree_with_none(tree_values)     # 리스트로 트리 구성

p = find_node(root, 6)  # 값 6에 해당하는 노드 찾기
q = find_node(root, 4)  # 값 4에 해당하는 노드 찾기

ancestor = LCA(root, p, q)  # 최소 공통 조상 찾기

print("LCA value:", ancestor.value if ancestor else "None")  # 결과 출력
