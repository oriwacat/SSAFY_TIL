import sys

sys.stdin = open('algo1_sample_in.txt', 'r')
from collections import deque

def kruscal(visited):
    global cnt, l_cnt
    queue = deque()
    for i in box:
        queue.append(i)  # 간선정보가 이중 리스트라 하나 벗기고 queue에 삽입
    while queue:
        x, y, w = queue.popleft()  # x(출발), y(도착) : 이동간선, w : 에너지
        if visited[x] and visited[y]:  # x, y 가 둘 다 방문 됐다는 건 이미 다른 간선을 통해 최소 에너지로 방문했다는 걸 의미
            continue
        cnt += w  # 둘 중 하나라도 방문 안했으면 연결하며 에너지 합산
        l_cnt += 1  # 간선 갯수 카운트
        visited[x] = True
        visited[y] = True

tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0  # 총 에너지 비용
    l_cnt = 0  # 모든 뉴런 연결되어 있는 지 확인용(n-1이 나와야 모든 뉴런 연결된걸로 판단)
    box.sort(key = lambda j: j[2])  # 에너지를 기준으로 정렬
    visited = [False] * (n+1)
    kruscal(visited)
    if l_cnt != n-1:
        print(f"#{t} -1")
    else:
        print(f"#{t} {cnt}")




