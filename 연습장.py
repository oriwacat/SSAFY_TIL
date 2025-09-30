from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
queue = deque()
dxy = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs():

    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if (x, y) == (n-1, m-1):
                return

            if 0 > nx or n <= nx or 0 > ny or m <= ny: continue
            if visited[nx][ny]: continue
            if a[nx][ny] == 0: continue

            visited[nx][ny] = True
            queue.append((nx,ny))


bfs()

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)