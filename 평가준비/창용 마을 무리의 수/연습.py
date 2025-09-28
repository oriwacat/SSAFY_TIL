import sys
from collections import defaultdict
sys.stdin = open('s_input.txt')

def dfs(i):
    visited[i] = True
    for x in p[i]:
        if not visited[x]:
            dfs(x)


T = int(input())

for t in range(1, T+1):
    n, m = map(int,input().split())
    p = defaultdict(list)
    cnt = 0
    visited = [False] * (n + 1)

    for i in range(m):
        x, y = map(int, input().split())
        p[x].append(y)
        p[y].append(x)
    for i in range(1, n+1):
        if visited[i] == False:
            dfs(i)
            cnt += 1
    print(f'#{t} {cnt}')