import sys
sys.stdin = open('sample_in.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    Hill = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    x = (1, -1, 0, 0)
    y = (0, 0, 1, -1)

    for i in range(N):
        for j in range(N):
            cnt = 1
            pos = Hill[i][j]

            while True:

                for k in range(4):
                    dx = x[k] + i
                    dy = y[k] + j
                    if 0 <= dx < N and 0 <= dy < N:
                        if pos > Hill[dx][dy]:
                            pos = Hill[dx][dy]
                            ni, nj = dx, dy
                if i == ni and j == nj:
                    break
                i, j = ni, nj
                cnt += 1
            result = max(cnt, result)
    print(f'#{t} {result}')