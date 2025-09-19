import pprint
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

dxy = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(grid[r][c]):
    for t in range(4):
        x,y = dxy[t]
        dx = r + x + (i*1)
        dy = r + y + (i*1)
        if 0 <= dx < n and 0 <= dy < n:
            grid[dx][dy] = 0

grid[r][c] = 0
pprint.pprint(grid)
adadwdaadawadwawda