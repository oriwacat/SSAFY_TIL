import sys
sys.stdin = open('sample_input.txt')

# class TreeNode:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
#
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.val)

T = int(input())

for t in range(1, T+1):
    N,M,L = map(int,input().split())
    tree = [0] * (N+1)
    for i in range(M):
        x,y = map(int,input().split())
        tree[x] = y


    for j in range(N,1, -1):
        tree[j//2] += tree[j]

    print(f'#{t} {tree[L]}')
