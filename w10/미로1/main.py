import sys
from collections import deque
sys.stdin = open('input.txt')
dxy = [[0,1],[1,0],[-1,0],[0,-1]]
def maze_runner(maze, n):
    queue = deque()
    queue.append((1,1))

    distance = [[-1]*n for _ in range(n)]
    distance[1][1] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if not(0 <= nx < n and 0 <= ny < n): continue
            if not distance[nx][ny] == -1: continue
            if maze[nx][ny] != 0 and maze[nx][ny] != 3: continue
            queue.append((nx,ny))
            distance[nx][ny] = distance[x][y] + 1

            if maze[nx][ny] == 3:
                return distance[nx][ny]

T = 10
for t in range(1, T+1):
    a = input()
    n = int(16)
    maze = [list(map(int,input())) for _ in range(n)]
    result = maze_runner(maze, n)
    if result:
        end = 1
    else:
        end = 0

    print(f'#{t} {end}')