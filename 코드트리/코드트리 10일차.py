n = int(input())
picked = []
visited = [False] * (n + 1)

# Please write your code here.
def pick(cnt):
    # 종료조건
    if cnt == n:
        print(*picked)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        picked.append(i)
        pick(cnt + 1)

        visited[i] = False
        picked.pop()

pick(0)
------------------------------

n = int(input())
picked = []
visited = [False] * (n + 1)

# Please write your code here.
def pick(cnt):
    # 종료조건
    if cnt == n:
        print(*picked)
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue

        visited[i] = True
        picked.append(i)
        pick(cnt + 1)

        visited[i] = False
        picked.pop()

pick(0)

---------------------
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
result = 0
ans = 0


# Please write your code here.

def pick(row):
    global ans
    global result
    if row == n:
        ans = max(ans, result)
        return

    for col in range(n):
        if visited[col] == 0:
            visited[col] = 1
            result += grid[row][col]

            pick(row + 1)

            result -= grid[row][col]
            visited[col] = 0


pick(0)
print(ans)


----------------------------

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
picked = []
col_visited = [False] * (n + 1)
ans = 0

def get_area():
    ret = 0
    for y, x in picked:
        ret += grid[y][x]
    return ret

def pick(row):
    global ans

    # 마지막 row까지 다 골랐다면
    if row == n:
        area = get_area()
        ans = max(ans, area)
        return

    # 현재 row에서 고른다.
    for i in range(0, n):
        if col_visited[i]:
            continue

        picked.append((row, i))
        col_visited[i] = True

        pick(row + 1)

        picked.pop()
        col_visited[i] = False

pick(0)
print(ans)

----------------------------
