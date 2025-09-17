import sys
sys.stdin = open('sample_input.txt')
from collections import defaultdict

# 후위순회로 구현하면 됩니다.
def dfs(v):
    # 현재 정점을 방문했다고 표시
    visited[v] = True

    # 인접한 정점들을 다시 dfs 호출
    for neighbor in graph[v]:
        # 방문한 적이 없는 인접 정점들만 DFS 시행
        if not visited[neighbor]:
            # 실행되면서 제일 안쪽으로 파고든다.
            dfs(neighbor)

    # 더 이상 파고들 때가 없는 경우에, 현재 정점을 결과에 추가한다.
    result.append(v)


T = 10
for tc in range(1, T + 1):
    v_cnt, e_cnt = map(int, input().split())
    edges = list(map(int, input().split()))

    # DAG 그래프 구성
    # 인접리스트 형태로 만들거다.
    graph = defaultdict(list)
    # 시작점과 끝정점을 서로 연결해준다.
    for i in range(e_cnt):
        graph[edges[2*i]].append(edges[2*i+1])

    # 방문여부를 체크해야 한다.
    visited = [False] * (v_cnt + 1)
    result = []

    """
    모든 정점에 대해서 DFS를 실행한다. 
    - 연결되지 않은 그래프가 주어졌을 때도, 모두 방문할 수 있도록 
    (각 연결된 부분끼리의 순서만 올바르게 유지되면 아무 문제가 없다 )
    => 그렇기 때문에 결과가 유일성 보장이 안된다는 겁니다. 
    """
    for v in range(1, v_cnt + 1):
        if not visited[v]:  # 방문하지 않은 정점에서만 DFS를 돌린다.
            dfs(v)

    print(f"#{tc}", *result[::-1])
