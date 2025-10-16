import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    e, n = map(int, input().split())
    box = list(map(int, input().split()))
    tree = {i: [] for i in range(1, e+2)}
    for i in range(0,len(box),2):
        tree[box[i]].append(box[i+1])
    # print(tree)
    cnt = 0
    q = [n]

    while q:
        x = q.pop()
        cnt += 1
        q.extend(tree[x])
    print(f'#{t} {cnt}')