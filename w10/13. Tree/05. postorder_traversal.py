class TreeNode:
    def __init__(self, key):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = key  # 노드의 값

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)  # 왼쪽 서브트리 방문
        postorder_traversal(root.right)  # 오른쪽 서브트리 방문
        print(root.val)  # 현재 노드 방문

# 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

postorder_traversal(root)  # 4 5 2 3 1
