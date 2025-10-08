n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1
cnt = 0
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while cnt < k:
    max_val = -1
    next_pos = (r, c)

    for dx, dy in dxy:
        nx, ny = r + dx, c + dy
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] > max_val:
                max_val = grid[nx][ny]
                next_pos = (nx, ny)

    r, c = next_pos
    cnt += 1

print(r + 1, c + 1)