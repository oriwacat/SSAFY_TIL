import sys
sys.stdin = open('algo1_sample_in.txt')
<<<<<<< HEAD
from collections import deque

def kal(visited):
    global l_lst,energy
    queue = deque()
    for i in box:
        queue.append(i)

    while queue:
        x,y,e = queue.popleft()

        if visited[x] and visited[y]: continue
        l_lst += 1
        energy += e
        visited[x] = True
        visited[y] = True

def kal2(box,visited):
    global l_lst, energy

    for x,y,e in box:
        if visited[x] and visited[y]: continue
        l_lst += 1
        energy += e
        visited[x] = True
        visited[y] = True



=======
import heapq
>>>>>>> 41fa8a02e54979a01a2800d2a5809697e2832283

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