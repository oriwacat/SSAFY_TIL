import sys
sys.stdin = open("input.txt")

T = int(input().strip())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    doll = list(map(int, input().split()))
    for _ in range(M): # 뒤집기 횟수
        i, j = map(int, input().split())
        for x in range(1, j+1):
            dm = (i-1) - x
            dp = (i-1) + x
            if 0 <= dm and dp < N and doll[dm] == doll[dp]:
                doll[dm] = 1 - doll[dm]
                doll[dp] = 1 - doll[dp]




    print(f'#{test_case}',*doll)
