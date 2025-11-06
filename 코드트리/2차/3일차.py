n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]


def shift(line, wind_dir):
    if wind_dir == 'L':
        # 오른쪽으로 한 칸씩 이동
        tmp = a[line][m - 1]

        for i in range(m - 1, 0, -1):
            a[line][i] = a[line][i - 1]

        a[line][0] = tmp

    else:
        # 왼쪽으로 한 칸씩 이동
        tmp = a[line][0]

        for i in range(0, m - 1, 1):
            a[line][i] = a[line][i + 1]

        a[line][m - 1] = tmp


def check(target, base):
    for i in range(m):
        if a[target][i] == a[base][i]:
            return True

    return False


def reverse(q):
    if q == 'L':
        return 'R'
    return 'L'


for r, q in winds:
    # r열을 d의 반대방향으로 한칸씩 이동
    init_r = r - 1
    init_q = q

    shift(init_r, init_q)
    curr_q = reverse(init_q)

    # 위로는 r-1, r-2, ..., 1번째 열까지 전파 (중간에 특정 조건에 따라 전파가 중단되기도 함)
    for k in range(init_r - 1, -1, -1):
        if check(k, k + 1):
            shift(k, curr_q)
            curr_q = reverse(curr_q)
        else:
            break

    curr_q = reverse(init_q)

    # 아래로는 i+1, i+2, ..., n번쨰 열까지 전파 (중간에 특정 조건에 따라 전파가 중단되기도 함)
    for k in range(init_r + 1, n, 1):
        if check(k, k - 1):
            shift(k, curr_q)
            curr_q = reverse(curr_q)
        else:
            break

for y in range(n):
    for x in range(m):
        print(a[y][x], end=" ")
    print()


    ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    dys = [0, -1, -1, 1, 1]
    dxs = [0, 1, -1, -1, 1]

    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    r, c, m1, m2, m3, m4, d = map(int, input().split())

    snapshot = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            snapshot[y][x] = grid[y][x]

    # d = 0 > 반시계로 회전 (예제 상황)
    # d = 1 > 시계로 회전

    # y, x에서 시작, ny, nx로 이동
    curr_y, curr_x = r - 1, c - 1

    if d == 0:
        for i in range(m1):
            ny = curr_y + dys[1]
            nx = curr_x + dxs[1]
            grid[ny][nx] = snapshot[curr_y][curr_x]
            curr_y, curr_x = ny, nx

        for i in range(m2):
            ny = curr_y + dys[2]
            nx = curr_x + dxs[2]
            grid[ny][nx] = snapshot[curr_y][curr_x]
            curr_y, curr_x = ny, nx

        for i in range(m3):
            ny = curr_y + dys[3]
            nx = curr_x + dxs[3]
            grid[ny][nx] = snapshot[curr_y][curr_x]
            curr_y, curr_x = ny, nx

        for i in range(m4):
            ny = curr_y + dys[4]
            nx = curr_x + dxs[4]
            grid[ny][nx] = snapshot[curr_y][curr_x]
            curr_y, curr_x = ny, nx

    else:
        for i in range(m4):
            ny = curr_y + dys[2]
            nx = curr_x + dxs[2]
            grid[ny][nx] = snapshot[curr_y][curr_x]
            curr_y, curr_x = ny, nx

        for i in range(m3):
            ny = curr_y + dys[1]
            nx = curr_x + dxs[1]
            grid[ny][nx] = snapshot[curr_y][curr_x]
            curr_y, curr_x = ny, nx

        for i in range(m2):
            ny = curr_y + dys[4]
            nx = curr_x + dxs[4]
            grid[ny][nx] = snapshot[curr_y][curr_x]
            curr_y, curr_x = ny, nx

        for i in range(m1):
            ny = curr_y + dys[3]
            nx = curr_x + dxs[3]
            grid[ny][nx] = snapshot[curr_y][curr_x]
            curr_y, curr_x = ny, nx

    for y in range(n):
        for x in range(n):
            print(grid[y][x], end=" ")
        print()
