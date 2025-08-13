import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T + 1):
    N, T1, T2 = map(int, input().split())
    block = list(map(int, input().split()))
    block = sorted(block)
    cnt1 = 0
    cnt2 = 0
    cnt = 0
    result = 0
    for i in range(1, N+1):
        if T1 > cnt1:
            result += i * block.pop()
            cnt1 += 1
            cnt += 1
        if T2 > cnt2:
            result += i * block.pop()
            cnt2 += 1
            cnt += 1
        if cnt == N:
            break
    print(f'#{t} {result}')

    