import sys
from collections import deque
sys.stdin = open('practice_input.txt')

dxy = [[1,0], [0,1],[-1,0],[0,-1]]
def get_road_move_time(road, n, m):
    queue = deque()
    queue.append((0,0,0))
    road[0][0] = 0

    while queue:
        x,y,dist = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y +dy
            next_dist = dist + 1

            if 0 <= nx < n and 0 <= ny < m and road[nx][ny] == 1:
                queue.append((nx,ny, next_dist))
                road[nx][ny] = 0

                if nx == n-1 and ny == m-1:
                    return next_dist


# 도로의 크기 n * m 입력 받기
n, m = map(int, input().split())
road = [list(map(int, input())) for _ in range(n)]  # 도로 정보 입력
result = get_road_move_time(road, n, m)  # BFS를 이용해서 이동시간 구하기
print(result)
