from collections import deque
import sys
sys.stdin = open('C:\\Users\\SSAFY\\Desktop\\a\\SSAFY_TIL\\평가준비\\창용 마을 무리의 수\\s_input.txt')

def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    count = 0

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)
            count += 1

    print(f'#{t} {count}')