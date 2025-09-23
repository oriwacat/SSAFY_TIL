k, n = map(int, input().split())
picked = []

def pick(cnt):
    # 종료조건
    if cnt == n:
        print(*picked)
        return

    # 숫자를 하나 고른다.
    for i in range(1, k + 1):
        picked.append(i)
        pick(cnt + 1)
        picked.pop()

# 하나의 숫자를 고른다. => n번의 재귀호출이 일어나야 한다.
pick(0)

---------------------------------------------

n = int(input())
number = []
ans = 0

def is_beautiful():
    curr_idx = 0
    for i in range(1, n):
        if number[curr_idx] == number[i]:
            continue
        else:
            cnt = i - curr_idx
            if cnt % number[curr_idx] != 0:
                return False
            curr_idx = i

    cnt = n - curr_idx

    if cnt % number[curr_idx] != 0:
        return False

    return True

def pick(cnt):
    global ans

    # 종료조건
    if cnt == n:
        if is_beautiful():
            ans += 1
        return

    # cnt + 1번째 숫자를 골라야 한다.
    for i in range(1, 5):
        number.append(i)
        pick(cnt + 1)
        number.pop() # 백트래킹


pick(0) # cnt: 현재 몇 번째 자리까지 골랐는지.
print(ans)

------------------------------------

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
bombs = []
res = 0


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def calculate():
    global res

    tmp = [[0] * n for _ in range(n)]
    cnt = 0

    for y in range(n):
        for x in range(n):
            if grid[y][x] == 0:
                continue

            tmp[y][x] = 1

            if grid[y][x] == 1:
                dys = [-2, -1, 0, 1, 2]
                dxs = [0, 0, 0, 0, 0]

                for i in range(5):
                    ny = y + dys[i]
                    nx = x + dxs[i]

                    if not in_range(ny, nx):
                        continue

                    tmp[ny][nx] = 1

            elif grid[y][x] == 2:
                dys = [-1, 0, 1, 0]
                dxs = [0, 1, 0, -1]

                for i in range(4):
                    ny = y + dys[i]
                    nx = x + dxs[i]

                    if not in_range(ny, nx):
                        continue

                    tmp[ny][nx] = 1

            elif grid[y][x] == 3:
                dys = [-1, -1, 1, 1]
                dxs = [-1, 1, 1, -1]

                for i in range(4):
                    ny = y + dys[i]
                    nx = x + dxs[i]

                    if not in_range(ny, nx):
                        continue

                    tmp[ny][nx] = 1

    for y in range(n):
        for x in range(n):
            if tmp[y][x] == 1:
                cnt += 1

    res = max(res, cnt)


def recursion(b):
    if len(b) == 0:
        calculate()
        return

    y, x = b.pop()

    for i in range(1, 4):
        grid[y][x] = i
        recursion(b)

    b.append((y, x))


for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            bombs.append((y, x))

recursion(bombs)
print(res)