import sys
sys.stdin = open('input.txt')
from collections import defaultdict

def preorder(root):
    print(root, end=' ')

    if len(tree[root]) >= 1:
        preorder(tree[root][0])

    if len(tree[root]) == 2:
        preorder(tree[root][1])

def inorder(root):
    if len(tree[root]) >= 1:
        inorder(tree[root][0])

    print(root, end=' ')

    if len(tree[root]) == 2:
        inorder(tree[root][1])

def postorder(root):
    if len(tree[root]) >= 1:
        postorder(tree[root][0])

    if len(tree[root]) == 2:
        postorder(tree[root][1])

    print(root, end=' ')


v = int(input())
arr = list(map(int,input().split()))
tree = defaultdict(list)

for i in range(0, len(arr), 2):
    p, c = arr[i], arr[i+1]
    tree[p].append(c)

for key in tree:
    tree[key].sort()

preorder(arr[0])
print()
inorder(arr[0])
print()
postorder(arr[0])