import sys
sys.stdin = open('island_input.txt')
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
def dfs(x,y):
    island[x][y] = 0
    for dx, dy in dxy:
        nx,ny = dx+x,dy+y
        if 0 > nx or nx >= n or 0 > ny or ny >= m: continue
        if island[nx][ny] == 0: continue
        dfs(nx,ny)

n, m = map(int, input().split())
island = [list(map(int,input())) for _ in range(n)]
island_cnt = 0

for i in range(n):
    for j in range(m):
        if island[i][j] == 0: continue
        dfs(i,j)
        island_cnt += 1

print(island_cnt)