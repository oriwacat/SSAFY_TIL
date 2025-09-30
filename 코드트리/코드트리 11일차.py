from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs():
    q.append((0, 0))

    while q:
        # 꺼내고
        y, x = q.popleft()

        # 주위 탐색해서 넣고
        for i in range(4):
            ny = y + dys[i]
            nx = x + dxs[i]

            if not in_range(ny, nx):
                continue
            if a[ny][nx] == 0:
                continue
            if visited[ny][nx]:
                continue

            visited[ny][nx] = True
            q.append((ny, nx))

bfs()

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)