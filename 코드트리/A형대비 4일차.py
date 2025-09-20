# i
# 6
# 1
# 2
# 3
# 1
# 1
# 5
# 2 4
# 2 2
# o
# 2
# 1
# 5
# from collections import deque
# n = int(input())
# blocks = [int(input()) for _ in range(n)]
# s1, e1 = map(int, input().split())
# s2, e2 = map(int, input().split())
# blocks = deque(blocks)
# box = []
# box = deque(box)
# for i in range(1,n+1):
#     if s1 <= i <= e1:
#         blocks.popleft()
#     else:
#         box.append(blocks.popleft())
#
# for i in range(1,len(box)+1):
#     if s2 <= i <= e2:
#         box.popleft()
#     else:
#         blocks.append(box.popleft())
#
# print(len(blocks))
# for x in blocks:
#     print(x)


dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# (1) 터뜨린다.
power = grid[r][c]
grid[r][c] = 0

# 4방향을 power만큼 0으로 바꾼다.
for i in range(4):
    for p in range(power):
        y = r + dys[i] * p
        x = c + dxs[i] * p

        if not in_range(y, x):
            continue

        grid[y][x] = 0

# (2) 중력에 의해 떨어진다.
for x in range(n):
    arr = []
    for i in range(n - 1, -1, -1):
        arr.append(grid[i][x])

    zero_idx = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[zero_idx] = arr[i]
            zero_idx += 1
    for i in range(zero_idx, len(arr)):
        arr[i] = 0

    arr = arr[::-1]

    for i in range(0, n):
        grid[i][x] = arr[i]

for y in range(n):
    for x in range(n):
        print(grid[y][x], end=" ")
    print()


# n: 숫자의 개수, m: 연속해서 m개 이상일 때 폭탄이 터짐.
n, m = tuple(map(int, input().split()))
numbers = [int(input()) for _ in range(n)]


def get_last_idx(idx, num):
    for i in range(idx + 1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            return i - 1

    return len(numbers) - 1


while True:
    explode = False

    for idx in range(len(numbers)):
        num = numbers[idx]

        if num == 0:
            continue

        # 만약 num이 m개 이상 반복된다면
        # 터뜨린다. => numbers[i]=0으로 만들어준다.
        last_idx = get_last_idx(idx, num)

        cnt = last_idx - idx + 1  # 연속되는 개수
        if cnt >= m:
            explode = True
            for i in range(idx, last_idx + 1):
                numbers[i] = 0

    tmp = []
    for i in range(len(numbers)):
        if numbers[i] != 0:
            tmp.append(numbers[i])
    numbers = tmp[::]

    if not explode:
        break

print(len(numbers))
for i in range(len(numbers)):
    print(numbers[i])


ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1
dxy = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(1,grid[r][c]):
    for t in range(4):
        x,y = dxy[t]
        dx = r + (x * i)
        dy = c + (y * i)
        if 0 <= dx < n and 0 <= dy < n:
            grid[dx][dy] = 0

grid[r][c] = 0

grid = [list(row) for row in zip(*grid[::-1])]

for g_list in grid:
    for i in range(n-1,0,-1):
        if g_list[i] == 0:
            g_list.pop(i)
            g_list.append(0)
    if g_list[0] == 0:
        g_list.pop(0)
        g_list.append(0)

grid = list(zip(*grid))[::-1]
for a in grid:
    for b in a:
        print(b,end=' ')
    print()