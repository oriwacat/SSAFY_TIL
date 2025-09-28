import sys
from collections import deque
sys.stdin = open('island_input.txt')

dxy = [(-1, 0), (1,0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
def find_island(island, x, y):
    queue = deque()
    queue.append((x,y))
    island[x][y] = 0

    while queue:
        cx ,cy = queue.popleft()

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if island[nx][ny] == 0: continue
            queue.append((nx,ny))
            island[nx][ny] = 0

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
island_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0: continue
        find_island(arr,i,j)
        island_cnt += 1

print(island_cnt)
