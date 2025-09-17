# current:탐색 정점 
# adjMatrix: 인접 행렬 
# visited: 방문 체크 리스트: 
def dfs(current, adj_matrix, visited):
    visited[current] = True  # 현재 정점을 방문했다고 표시

    for i in range(len(adj_matrix)):  # 모든 정점에 대해
        # 현재 정점과 연결되어 있고, 아직 방문하지 않은 정점이라면
        if adj_matrix[current][i] and not visited[i]:  
            dfs(i, adj_matrix, visited)  # 그 정점을 방문

# 정점 수: N
N = 5
# 인접 행렬
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

# 방문 체크 배열 초기화
visited = [False] * N  # 모든 정점을 아직 방문하지 않았다고 표시

# 연결되지 않은 정점도 방문하기 위해서 모든 정점에 대해서 dfs 실행
for i in range(N):
    if visited[i]: continue
    # 시작 정점: 0
    dfs(0, adj_matrix, visited)  # 깊이 우선 탐색 시작
