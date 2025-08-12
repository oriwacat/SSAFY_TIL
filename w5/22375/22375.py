import sys
sys.stdin = open("switch_sample_in.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))
    i = 0
    cnt = 0
    while before != after:
        if before[i] != after[i]:
            for x in range(i, N):
                if before[x] == 0:
                    before[x] = 1
                else:
                    before[x] = 0
            cnt += 1
        i += 1

    print(f'#{test_case} {cnt}')

