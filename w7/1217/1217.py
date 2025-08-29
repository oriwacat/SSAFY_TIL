import sys
sys.stdin = open('input.txt')

def exponentiation(N, M):
    if M == 1:
        return N

    return N * exponentiation(N, M-1)
T = 10
for t in range(1, T+1):
    h = int(input())
    N, M = map(int, input().split())
    print(f'#{h} {exponentiation(N, M)}')