import sys
sys.stdin = open("s_input.txt")

T = int(input())
for tc in range(1, T + 1):
    stops = [0] * 5001
    result = []
    N = int(input())
    for i in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            stops[i] += 1
    P = int(input())
    for i in range(P):
        C = int(input())
        result.append(stops[C])

    print(f'#{tc}',*result)



