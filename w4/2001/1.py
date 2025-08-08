import sys
sys.stdin = open("input.txt")

T = int(input().strip())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for i in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            xx = 0

            for x in range(M):
                for y in range(M):
                    dx = i + x
                    dy = j + y
                    if 0 <= dx < N and 0 <= dy < N:
                        xx += matrix[dx][dy]
            
            result.append(xx)
    print(f'#{test_case} {max(result)}')