import sys
from collections import defaultdict
sys.stdin = open('sample_input.txt')

def dfs(start, end, visited):
    # global result
    visited[start] = True
    # if edges[start] == end:
    #     result = 1
    for x in edges[start]:
        if not visited[x]:
            dfs(x, end, visited)

T = int(input())

for t in range(1, T+1):
    result = 0
    V, E = map(int,input().split())
    edges = defaultdict(list)
    visited = [False] * (V+1)
    for _ in range(E):
        x, y = map(int,input().split())
        edges[x].append(y)
    st, en = map(int,input().split())

    dfs(st, en, visited)
    if visited[en] == True:
        result = 1
    print(f'#{t} {result}')