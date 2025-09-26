import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T+1):
    power, N, M = map(int,input().split())
    station = list(map(int,input().split()))
    temp = 0
    cnt = 0

    for i in range(N + 1):
        result = False

        if temp != i:
            continue

        if N <= power + temp:
            break

        for j in range(i + 1, power + i + 1):
            if j in station:
                temp = j
                result = True

        if not result:
            cnt = 0
            break
        cnt += 1
    print(f'#{t} {cnt}')