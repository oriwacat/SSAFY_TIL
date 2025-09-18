import sys
from collections import deque
sys.stdin = open('practice_input.txt')
import pprint
dxy = [[1,0], [0,1],[-1,0],[0,-1]]
def get_road_move_time(road, n, m):
    queue = deque()
    queue.append((0,0))

    distance =[[-1] * m for _ in range(n)]
    distance[0][0] = 0

    while queue:
        x,y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if not(0 <= nx < n and 0 <= ny < m): continue
            if not distance[nx][ny] == -1: continue
            if not road[nx][ny] == 1: continue
            queue.append((nx,ny))
            distance[nx][ny] = distance[x][y] + 1

            if nx == n-1 and ny == m-1:
                pprint.pprint(distance)
                return distance[nx][ny]

# 도로의 크기 n * m 입력 받기
n, m = map(int, input().split())
# 도로 정보 입력
road = [list(map(int, input())) for _ in range(n)]

# BFS를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)

print(result)
