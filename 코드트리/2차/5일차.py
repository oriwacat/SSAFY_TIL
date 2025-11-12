벽짚고 미로
N = int(input())
x, y = map(int, input().split())
d = 1
time = 0

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# 이동 불가능한 경우 => 반시계 회전

# 이동 가능한 경우
# - 이동했을 때, 밖이라면 => 끝

# - 겪자 안
# (1) 이동했을 때, 오른쪽에 벽이 있다 => 이동
# (2) 이동했을 때, 오른쪽에 벽이 없다 => 시계 회전 + 이동

# ============================

# 북 동 남 서
dys = [0, 1, 0, -1]
dxs = [-1, 0, 1, 0]


def in_range(curr_x, curr_y):
    return 1 <= curr_x <= N and 1 <= curr_y <= N


def move(curr_x, curr_y, curr_dir):
    nx = curr_x + dxs[curr_dir]
    ny = curr_y + dys[curr_dir]

    return nx, ny


def turn(curr_dir, l_or_r):
    if l_or_r == 'L':
        return (curr_dir + 3) % 4
    else:
        return (curr_dir + 1) % 4


def can_move(curr_x, curr_y, curr_dir):
    target_x = curr_x + dxs[curr_dir]
    target_y = curr_y + dys[curr_dir]

    if not in_range(target_x, target_y):
        return True

    if grid[target_x][target_y] == '#':
        return False

    return True


def has_wall_on_the_right(curr_x, curr_y, curr_dir):
    right_dir = (curr_dir + 1) % 4

    target_x = curr_x + dxs[right_dir]
    target_y = curr_y + dys[right_dir]

    if not in_range(target_x, target_y):
        return True  # need to check

    if grid[target_x][target_y] == '#':
        return True

    return False


time = 0
visited = set()

while True:
    if (x, y, d) in visited:
        time = -1
        break

    visited.add((x, y, d))

    if can_move(x, y, d):
        x, y = move(x, y, d)
        time += 1

        if not in_range(x, y):
            break

        if not has_wall_on_the_right(x, y, d):
            d = turn(d, 'R')
            x, y = move(x, y, d)
            time += 1

    else:
        d = turn(d, 'L')

print(time)

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
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