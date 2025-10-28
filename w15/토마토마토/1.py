from collections import deque

dxyz = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]  # 위, 아래, 상, 하, 앞, 뒤

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()

# 초기 익은 토마토 좌표를 큐에 저장
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 1:
                q.append((z, x, y))

# BFS
while q:
    z, x, y = q.popleft()
    for dz, dx, dy in dxyz:
        nz, nx, ny = z + dz, x + dx, y + dy
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and arr[nz][nx][ny] == 0:
            arr[nz][nx][ny] = arr[z][x][y] + 1  # 하루 증가
            q.append((nz, nx, ny))

# 결과 계산
days = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 0:  # 안 익은 토마토가 있으면
                print(-1)
                exit(0)
            days = max(days, arr[z][x][y])

print(days - 1)
