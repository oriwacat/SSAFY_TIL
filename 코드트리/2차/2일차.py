n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
res = -999999

def overlap(y1, y2, x1, x2, y3, y4, x3, x4):
    y_overlap = y1 <= y3 <= y2 or y3 <= y1 <= y4
    x_overlap = x1 <= x3 <= x2 or x3 <= x1 <= x4
    return y_overlap and x_overlap

def get_sum(y1, y2, x1, x2):
    s = 0
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            s += grid[y][x]
    return s

# 한 개의 사각형을 먼저 fix하고,
# 나머지 사각형을 만든다.
# => 겹치면 continue
# => 겹치지 않으면 합 계산

for y1 in range(0, n):
    for y2 in range(y1, n):
        for x1 in range(0, m):
            for x2 in range(x1, m):

                for y3 in range(0, n):
                    for y4 in range(y3, n):
                        for x3 in range(0, m):
                            for x4 in range(x3, m):

                                if overlap(y1, y2, x1, x2, y3, y4, x3, x4):
                                    continue

                                res = max(res, get_sum(y1, y2, x1, x2) + get_sum(y3, y4, x3, x4))

print(res)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
res = -999999

def overlap(y1, y2, x1, x2, y3, y4, x3, x4):
    y_overlap = y1 <= y3 <= y2 or y3 <= y1 <= y4
    x_overlap = x1 <= x3 <= x2 or x3 <= x1 <= x4
    return y_overlap and x_overlap

def get_sum(y1, y2, x1, x2):
    s = 0
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            s += grid[y][x]
    return s

# 한 개의 사각형을 먼저 fix하고,
# 나머지 사각형을 만든다.
# => 겹치면 continue
# => 겹치지 않으면 합 계산

for y1 in range(0, n):
    for y2 in range(y1, n):
        for x1 in range(0, m):
            for x2 in range(x1, m):

                for y3 in range(0, n):
                    for y4 in range(y3, n):
                        for x3 in range(0, m):
                            for x4 in range(x3, m):

                                if overlap(y1, y2, x1, x2, y3, y4, x3, x4):
                                    continue

                                res = max(res, get_sum(y1, y2, x1, x2) + get_sum(y3, y4, x3, x4))

print(res)