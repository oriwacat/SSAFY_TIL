dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

t = 0
curr_dir = 0
visited = set()

def in_range(i, j):
    return 1 <= i <= N and 1 <= j <= N

while True:
    if (x, y, curr_dir) not in visited:
        visited.add((x, y, curr_dir))
    else:
        print(-1)
        exit()

    nx = x + dxs[curr_dir]
    ny = y + dys[curr_dir]

    # 격자 밖 > 탈출
    if not in_range(nx, ny):
        x, y = nx, ny
        t += 1
        print(t)
        exit()

    if grid[nx][ny] == '#':
        curr_dir  = (curr_dir + 1) % 4
        continue

    # 이동 가능한 경우
    x, y = nx, ny
    t += 1

    # 회전 가능여부 파악
    check_dir = (curr_dir + 3) % 4
    check_x = x + dxs[check_dir]
    check_y = y + dys[check_dir]

    if in_range(check_x, check_y) and grid[check_x][check_y] == '.':
        curr_dir = check_dir