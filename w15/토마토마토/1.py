# import sys
# sys.stdin = open('input.txt')
from collections import deque
dxy = [(1,0),(-1,0),(0,1),(0,-1)]


m,n,h = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
cnt = 0

for z in range(h):
    for i in range(n):
        for j in range(m):
            if arr[z][i][j] != 1: continue
            q.append((z,i,j))
# print(q)
while q:
    z,x,y = q.popleft()
    for dx, dy in dxy:
        nx,ny = dx + x, dy + y
        if 0 > nx or nx >= n or 0 > ny or ny >= m: continue
        if arr[z][nx][ny] != 0: continue
        arr[z][nx][ny] = arr[z][x][y] + 1
        q.append((z,nx,ny))

    for dz in [1, -1]:  # 위아래 층 이동
        nz = z + dz
        if 0 <= nz < h and arr[nz][x][y] == 0:
            arr[nz][x][y] = arr[z][x][y] + 1
            q.append((nz, x, y))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 0:
                print(-1)
                exit()
            cnt = max(cnt, arr[z][x][y])
print(cnt-1)

