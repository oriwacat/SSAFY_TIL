import sys
from collections import defaultdict
sys.stdin = open('s_input.txt')

# DFS 방문하는 함수
def dfs(start_vertex):
    # 1. 해당 노드 방문 처리!
    visited[start_vertex] = True

    # 2. 인접 노드들을 순회하면서, 방문한 적없는 정점에 대해서 DFS
    for adj_v in graph[start_vertex]:  # 인접합 노드들 가져오죠..
        if not visited[adj_v]:
            dfs(adj_v)

T = int(input())
for test_case in range(1, 2):
    # 마을에 사는 사람 수, 관계 수
    # vertex 수, edge 수
    N, M = map(int, input().split())
    # DFS => 인접한 정점에 접근해야한다.
    # 인접 리스트 형태가 좋다! { 'A': ['B', 'C', 'D'], ... }
    graph = defaultdict(list)
    # 양방향 그래프니까, 양쪽에서 서로 연결해야 한다.
    for _ in range(M):
        start_v, end_v = map(int, input().split())
        graph[start_v].append(end_v)  # start_v => end_v
        graph[end_v].append(start_v)  # end_v => start_v

    # 그룹의 개수
    group_cnt = 0
    # 그래프에서 DFS를 할 때는 뭘 해야한다 ?
    # 1. 방문처리를 해야한다. (visited)
    # 2. 모든 정점에 대해서 DFS를 실행해야 한다.
    visited = [False] * (N + 1)  # 정점의 개수만큼 초기화
    for i in range(1, N+1):  # 모든 정점에 대해서 DFS 실행
        if not visited[i]:  # 방문한 적이 없는 정점만 DFS
            dfs(i)
            # 새로운 DFS가 실행됐다는 건 => 새로운 무리가 찾아졌다는 겁니다.
            group_cnt += 1

    print(f"#{test_case} {group_cnt}")
