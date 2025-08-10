import sys
sys.stdin = open("input1.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    balloons = []
    result = 0
    xx = []
    for _ in range(N):
        balloons.append(list(map(int, input().split())))

    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    for i in range(N):
        for j in range(M):
            result = balloons[i][j]
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if 0 <= ni < N and 0<= nj < M:
                    result += balloons[ni][nj]
            xx.append(result)

    print(f'#{test_case} {max(xx)}')