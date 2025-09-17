# graph: 그래프를 나타내는 인접 리스트
# start: 탐색을 시작할 정점
# visited: 방문한 정점을 저장하는 집합
# result: 탐색 경로를 저장하는 리스트
def dfs(graph, start, visited, result):
    pass

# 그래프 인접 리스트
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'G'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['C', 'F']
}

start_vertex = 'A'
visited = set()  # 방문한 정점을 저장할 집합
result = []  # 탐색 경로를 저장할 리스트

dfs(graph, start_vertex, visited, result) 

print(' '.join(result))  # 탐색 경로 출력
