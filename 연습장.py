n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]


def go(a, side):
    if side == 'L':
        temp = a[m-1]

        for i in range(m - 1, 0, -1):
            a[i] = a[i -1]
        a[0] = temp
    else:
        temp = a[0]
        for i in range(m):
            a[i] = a[i+1]
        a[m] = temp

for _ in range(q):
    cnt = 1
    up = True
    down = True
    go(a[winds[0][0]], winds[0][1])
    while up == True or down == True:
        if up:
            for i in range(m):
                if a[winds[0][0]][i] == a[winds[0][0]+cnt][i]:
                    go(a[winds[0][0]], winds[0][1])

