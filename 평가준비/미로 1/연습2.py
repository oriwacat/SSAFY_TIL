import sys
from collections import deque
sys.stdin = open('input.txt')

dxy = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs():
    queue = deque()
    queue.append((1,1))
    visited[1][1] = True

    while queue:
        x,y = queue.popleft()

        for dx,dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 > nx or n <= nx or 0 > ny or n <= ny: continue
            if arr[nx][ny] == 1: continue
            if visited[nx][ny]: continue
            if arr[nx][ny] == 3: return 1
            queue.append((nx,ny))
            visited[nx][ny] = True

    return 0




T = 10
for t in range(1, T+1):
    _ = input()
    n = 16
    arr = [list(map(int,input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    ans = bfs()
    print(f'#{t} {ans}')