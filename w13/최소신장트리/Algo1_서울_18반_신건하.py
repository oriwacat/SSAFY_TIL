#  Prim 방식으로 해결하였습니다.
import sys

sys.stdin = open('algo1_sample_in.txt', 'r')
import heapq

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    adj_list = {i : {} for i in range(1, n+1)}  # 그래프 생성
    print(adj_list)
    for _ in range(m):
        x, y, v = map(int, input().split())
        adj_list[x][y] = v  # 양방향으로 삽입해줍니다.
        adj_list[y][x] = v  # 양방향으로 삽입해줍니다.
    # print(adj_list)
    visited = set()  # 방문처리용 visited
    min_heap = []
    heapq.heappush(min_heap, [0, 1])  # 가중치와 시작위치 우선순위큐에 삽입/ 시작위치는 어떤걸 선정해도 상관없어서 임의로 1번으로 선정했습니다.
    print(min_heap)
    ans = 0
    while min_heap:
        val, pos = heapq.heappop(min_heap)  # 우선순위 큐에 의해 최솟값인 가중치가 우선적으로 나오게 됩니다.

        if pos in visited:  # 방문 이력이 있으면 continue 합니다.
            continue

        visited.add(pos)  # 방문처리해줍니다.
        ans += val  # 정답에 가중치를 더해줍니다.

        for next_pos, weight in adj_list[pos].items():
            if next_pos not in visited:  # 해당 노드와 연결된 노드중 방문한 이력이 없는 노드만 넣어줍니다.
                heapq.heappush(min_heap, [weight, next_pos])

    if len(visited) == n:  # 방문이력의 길이가 n과 같으면 모든 뉴런이 연결됐다고 판단합니다.
        print(f"#{tc} {ans}")
    else:
        print(f"#{tc} -1")
