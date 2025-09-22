n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
k -= 1
trigger = True
while True:

    for i in range(n):
        if all(x == 0 for x in grid[i][k:m]):
            for j in range(k,m):
                grid[i][j] = 1
                if 0 <= grid[i-1][j] < n:
                    grid[i-1][j] = 0
                continue



    if trigger:
        break

print(grid)