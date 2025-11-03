n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# 북0 동1 남2 서3
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def get_start_dir(k):
    if 1 <= k <= n:
        return 2
    if n < k <= 2 * n:
        return 3
    if 2 * n < k <= 3 * n:
        return 0
    if 3 * n < k <= 4 * n:
        return 1

def get_start_pos(k):
    if 1 <= k <= n:
        return 0, k - 1
    if n < k <= 2 * n:
        return (k - 1) - n, n - 1
    if 2 * n < k <= 3 * n:
        return n - 1, 3 * n - k
    if 3 * n < k <= 4 * n:
        return 4 * n - k, 0

def reflect(y, x, d):
    mirror = grid[y][x]

    if mirror == '/':
        if d == 0:
            return 1
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        elif d == 3:
            return 2

    elif mirror == '\\':
        if d == 0:
            return 3
        elif d == 1:
            return 2
        elif d == 2:
            return 1
        elif d == 3:
            return 0

# k라는 값으로 출발 좌표, 출발 방향을 얻어낸다.
y, x = get_start_pos(k)
d = get_start_dir(k)
cnt = 0

while in_range(y, x):
    # 현재 좌표와 바라보고 있는 방향에 따라 반사될 방향이 결정
    d = reflect(y, x, d)
    cnt += 1
    y += dys[d]
    x += dxs[d]

print(cnt)