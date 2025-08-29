import sys
sys.stdin = open('sample_input.txt')
from collections import deque

T = int(input())

for t in range(1, T+1):
    N = int(input())
    card = list(input().split())
    A = card[:(N + 1) // 2]
    B = card[(N + 1) // 2:]
    result = []
    while len(result) < N:
        if A:
            result.append(A.pop(0))
        if B:
            result.append(B.pop(0))

    print(f'#{t} {" ".join(result)}')


