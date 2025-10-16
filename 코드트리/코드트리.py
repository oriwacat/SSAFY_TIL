from itertools import combinations
from collections import deque


def in_range(row, col):
    if row < 0 or row >= N or col < 0 or col >= N:
        return False

    if a[row][col] == WALL:
        return False

    if visited[row][col] != 0:
        return False

    return True


def bfs():
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    max_depth = 0

    while q:

        row, col, steps = q.popleft()
        if a[row][col] == VIRUS:
            max_depth = max(max_depth, steps)

        for i in range(4):
            nx, ny = row + dx[i], col + dy[i]
            if in_range(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny, steps + 1))

    for i in range(N):
        for j in range(N):
            if a[i][j] == VIRUS and visited[i][j] == 0:
                max_depth = INT_MAX

    return max_depth


N, M = tuple(map(int, input().split()))
q = deque()
VIRUS = 0
HOSPITAL = 2
WALL = 1
INT_MAX = 1000000
a = [
    list(map(int, input().split()))
    for _ in range(N)
]

hospitals = list()
selected_hos = list()

for i in range(N):
    for j in range(N):
        if (a[1][j] == HOSPITAL):
            hospitals.append((i, j))

visited = [
    [False for _ in range(N)]
    for _ in range(N)
]

steps = [
    [False for _ in range(N)]
    for _ in range(N)
]

ans = INT_MAX
num_of_hospital = len(hospitals)

nums = range(num_of_hospital)
for comb in combinations(nums, M):
    for hopital_idx in comb:
        row, col = hospitals[hopital_idx]
        q.append((row, col, 0))

    ans = min(ans, bfs())

if ans == INT_MAX:
    ans = -1

print(ans)
