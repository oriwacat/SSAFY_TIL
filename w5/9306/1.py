import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    M = list(map(int, list(input())))
    cnt = 0
    llen = 0

    for i in range(N):
        if M[i] == 1:
            llen += 1
            if cnt < llen:
                cnt = llen
        else:
            llen = 0

    print(f'#{test_case} {cnt}')
