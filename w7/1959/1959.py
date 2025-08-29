import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    f_list = list(map(int, input().split()))
    s_list = list(map(int, input().split()))
    result = 0

    if N >= M:
        for i in range(N-M+1):
            x = 0
            for j in range(M):
              x += f_list[j+i] * s_list[j]
            result = max(result, x)

    else:
        for i in range(M-N+1):
            x = 0
            for j in range(N):
                x += s_list[j + i] * f_list[j]
            result = max(result, x)

    print(f'#{t} {result}')