import sys
sys.stdin = open('sample_in.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    Hill = [list(map(int, input().split())) for _ in range(N)]

    x = (1, -1, 0, 0)
    y = (0, 0, 1, -1)

    for i in range(N):
        for j in range(N):
            cnt = 1
            pos = 10000
            while True:
                for k in range(4):
                    dx = x[k] + i
                    dy = x[k] + j
                    if 0 <= dx < N and 0 <= dy < N:
                        pos = min(pos, Hill[dx][dy])
                cnt += 1
