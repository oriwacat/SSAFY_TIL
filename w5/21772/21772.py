import sys
sys.stdin = open("5097_input.txt")
from collections import deque



T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    K = deque(map(int,input().split()))
    for i in range(M):
        K.append(K.popleft())
    print(f'#{test_case} {K[0]}')

