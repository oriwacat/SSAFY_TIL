n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

x = (-1,1,0,0)
y = (0,0,-1,1)
result = set()

for time in range(t):

    for i in range(m):
        nx, ny = 0, 0
        for k in range(4):
            dx = k + r[i]-1
            dy = k + c[i]-1
            if 0 <= dx < n and 0 <= dy < n:
                if a[dx][dy] > a[r[i]-1][c[i]-1]:
                    nx, ny = dx, dy
        result.add((nx, ny))
    print(len(result))
        # print(a[r[i]-1][c[i]-1])