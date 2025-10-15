import sys
sys.stdin = open('algo1_sample_in.txt')
import heapq

T = int(input())

for t in range(1, T+1):
    n,m = map(int,input().split())
    lst = {i : {} for i in range(1, n+1)}
    for _ in range(m):
        x,y,e = map(int,input().split())
        lst[x][y] = e
        lst[y][x] = e

    energy = 0
    visited = set()
    min_heap = []
    heapq.heappush(min_heap, [0,1])

    while min_heap:
        val, pos = heapq.heappop(min_heap)

        if pos in visited: continue

        visited.add(pos)
        energy += val

        for next_pos, eng in lst[pos].items():
            if next_pos in visited: continue
            heapq.heappush(min_heap, [eng, next_pos])

    if len(visited) == n:
        print(energy)
    else:
        print(-1)