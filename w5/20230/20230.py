import sys
sys.stdin = open("sample_in.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    x = (1, -1, 0, 0)
    y = (0, 0, 1, -1)
    max_result = 0
    for i in range(N):
        for j in range(N):
            result = matrix[i][j]
            for k in range(4):
                for q in range(1, N):
                    dx = i + (x[k] * q)
                    dy = j + (y[k] * q)
                    if 0 <= dx < N and 0 <= dy < N:
                        result += matrix[dx][dy]
            if max_result < result:
                max_result = result
    print(f'#{test_case} {max_result}')

