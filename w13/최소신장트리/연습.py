import sys
sys.stdin = open('algo1_sample_in.txt')
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




T = int(input())

for t in range(1, T+1):
    n,m = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(m)]
    energy = 0
    l_lst = 0
    visited = [False] * (n+1)
    box.sort(key = lambda x: x[2])
    # kal(visited)
    kal2(box,visited)

    if l_lst != n-1:
        print(f'#{t} {-1}')
    else:
        print(f'#{t} {energy}')