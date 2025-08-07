T = int(input().strip())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    balloons = []
    result = 0

    for i in range(N):
        balloons.append(list(map(int, input().split())))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(M):
            temp_sum = balloons[i][j]
            for k in range(4):
                for z in range(1, balloons[i][j] + 1):
                    ni = i + (dx[k] * z)
                    nj = j + (dy[k] * z)

                    if 0 <= ni < N and 0 <= nj < M:
                        temp_sum += balloons[ni][nj]

            if temp_sum > result:
                result = temp_sum

    print(f'#{test_case} {result}')