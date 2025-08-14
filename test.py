import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j]:
                cnt += 1
                continue
            if cnt == K:
                result += 1
            cnt = 0
        if cnt == K:
            result += 1
    for j in range(N):
        cnt = 0
        for i in range(N):
            if matrix[i][j]:
                cnt += 1
                continue
            if cnt == K:
                result += 1
            cnt = 0
        if cnt == K:
            result += 1
    print(f'#{tc} {result}')