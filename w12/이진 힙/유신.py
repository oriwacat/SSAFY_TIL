import sys
sys.stdin = open('sample_input.txt')
import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) - 1
    nums = list(map(int, input().split()))
    hq = []
    for n in nums:
        heapq.heappush(hq, n)
    answer = 0

    while N > 0:
        N = (N - 1) // 2
        answer += hq[N]

    print(f"#{tc} {answer}")