K, N = map(int, input().split())

picked = []

def pick(cnt):
    # 종료조건
    if cnt == N:
        print(*picked)
        return

    for i in range(1, K + 1):
        if (
            len(picked) >= 2 and
            picked[-2] == picked[-1] and
            i == picked[-1]
        ):
            continue

        picked.append(i)
        pick(cnt + 1)
        picked.pop()

pick(0)



-------------------------------------


# n: 턴의 수, m: 끝점의 좌표, k: 말의 수, nums: 턴마다 움직일 거리
n, m, k = map(int, input().split())
movings = list(map(int, input().split()))

positions = [1] * (k + 1)
ans = 0

def calc():
    # m에 도달한 말이 몇개인지 센다.
    cnt = 0
    for i in range(1, k + 1):
        if positions[i] >= m:
            cnt += 1
    return cnt

# idx는 moving의 index = 현재 몇 번쨰 움직임을 진행할지
def move(idx):
    global ans

    if idx == n:
        # print(movings)
        ans = max(ans, calc())
        return

    for i in range(1, k + 1):
        if k > 1 and positions[i] >= m:
            continue

        positions[i] += movings[idx] # i를 움직인다.
        move(idx + 1) # 재귀를 한다.
        positions[i] -= movings[idx] # i의 움직임을 돌려놓는다.

move(0)
print(ans)

-------------------------------------------------


n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

ans = 0

dys = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dxs = [0, 0, 1, 1, 1, 0, -1, -1, -1]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def get_movable_positions(y, x):
    curr_dir = move_dir[y][x]
    positions = []

    ny, nx = y, x
    while True:
        ny += dys[curr_dir]
        nx += dxs[curr_dir]

        if not in_range(ny, nx):
            break

        if num[ny][nx] > num[y][x]:
            positions.append((ny, nx))

    return positions

def move(cnt, y, x):
    global ans

    positions = get_movable_positions(y, x)

    # 종료조건? => 이동할 수 없을 때 (positions == 0)
    if len(positions) == 0:
        ans = max(ans, cnt)
        return

    # positions를 돌면서 이동시킨다.
    for ny, nx in positions:
        move(cnt + 1, ny, nx)


move(0, r - 1, c - 1)
print(ans)
