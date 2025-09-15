class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 후위 순회 실행
postorder(root)

