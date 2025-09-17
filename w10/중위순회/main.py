import sys
sys.stdin = open('input.txt')

class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def inoder_ans(root):
    global ans
    if root:
        inoder_ans(root.left)
        ans += tree[root.value]
        inoder_ans(root.right)

T = 10
for t in range(1, T+1):
    n = int(input())

    tree = [[]for _ in range(n + 1)]
    child = [[]for _ in range(n + 1)]
    for idx in range(n):
        q = list(map(str, input().split()))
        idx = int(q[0])
        val = q[1]

        tree[idx] = val
        for i in range(2, len(q)):
            child[idx].append(int(q[i]))

    nodes = [None] + [TreeNode(i) for i in range(1, n+1)]

    for i in range(1, n+1):
        kids = child[i]
        if len(kids) >= 1:
            nodes[i].left = nodes[kids[0]]
        if len(kids) == 2:
            nodes[i].right = nodes[kids[1]]

    root_idx = 1
    ans = ''
    inoder_ans(nodes[root_idx])
    print(ans)