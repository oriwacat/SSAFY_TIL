import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    doll = list(map(int, input().split()))
    for _ in range(M): # 뒤집기 횟수
        i, j = map(int, input().split())
        for x in range(1, j+1):
            dm = (i-1) - x
            dp = (i-1) + x
            if doll[dm] == doll[dp] and 0 <= dm and dp < N:
                if doll[dm] == 0:
                    doll[dm], doll[dp] = 1
                elif doll[dm] == 1:
                    doll[dm], doll[dp] = 0




    print(f'#{test_case} {cnt}')
