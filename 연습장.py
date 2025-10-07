n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1
cnt = 0
dxy = [(1,0),(-1,0),(0,1),(0,-1)]






while True:
    num = 0
    lst = []
    if cnt == k:
        break
    for dx, dy in dxy:

        nx, ny = r + dx, c + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if grid[nx][ny] > num:
            num = grid[nx][ny]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                lst.append((i, j))



    cnt += 1
