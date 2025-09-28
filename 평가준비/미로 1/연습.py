import sys
sys.stdin = open('input.txt')

dxy = [(1,0),(0,1),(-1,0),(0,-1)]
def dfs(x, y):
    if arr[x][y] == 3:
        return 1
    for dx,dy in dxy:
        nx = dx+x
        ny = dy+y
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if arr[nx][ny]: continue
        dfs(nx, ny)


T = 10
for t in range(1, T+1):
    _ = input()
    n = 16
    arr = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si,sj = i,j

    ans = dfs(si, sj)
    print(ans)