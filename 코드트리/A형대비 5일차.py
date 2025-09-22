# 상하좌우
dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]

N, r, c = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]
r -= 1
c -= 1

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def can_move():
    # 상하좌우를 탐색하면서 더 큰 값이 있는지를 확인
    # 더 큰 값이 있다고 하면, 그 방향을 리턴
    # 더 큰 값이 없으면 -1을 리턴
    for i in range(4):
        ny = r + dys[i]
        nx = c + dxs[i]

        if not in_range(ny, nx):
            continue

        if grid[r][c] < grid[ny][nx]:
            return i

    return -1

def move(d):
    global r, c

    ny = r + dys[d]
    nx = c + dxs[d]

    r, c = ny, nx

print(grid[r][c], end=" ")

while True:
    d = can_move()

    if d != -1:
        move(d)
        print(grid[r][c], end=" ")
    else:
        break


# 내코드 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
n, r, c = map(int, input().split())
r -= 1
c -= 1
a = [list(map(int, input().split())) for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
trigger = False
result = []
while True:
    trigger = True
    for i in range(4):
        dx, dy = dxy[i]
        x = r + dx
        y = c + dy
        if 0 <= x < n and 0 <= y < n and a[x][y] > a[r][c]:
            result.append(a[r][c])
            r = x
            c = y
            trigger = False
            break

    if trigger:
        result.append(a[r][c])
        break

print(*result)
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


N, M, K = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]


def can_move(r):
    # 1. 바닥에 닿는지.
    if r == N - 1:
        return False

    # 2. 바로 밑에 다른 블럭이 있는지
    for i in range(K - 1, K + M - 1):
        if grid[r + 1][i] == 1:
            return False

    return True


def move(r):
    for i in range(K - 1, K + M - 1):
        if r >= 0:
            grid[r][i] = 0
        grid[r + 1][i] = 1


r = -1
while True:
    if can_move(r):
        move(r)
        r += 1
    else:
        break

for y in range(N):
    for x in range(N):
        print(grid[y][x], end=" ")
    print()

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#내코드

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
k -= 1
trigger = True

while True:
    for i in range(n):
        if all(x == 0 for x in grid[i][k:k+m]):
            for j in range(k,k+m):
                grid[i][j] = 1
                if 0 <= i-1< n:
                    grid[i-1][j] = 0
            continue
        else:
            break

    if trigger:
        break
for result in grid:
    print(*result)
--------------------------------------------

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
