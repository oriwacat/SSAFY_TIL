from collections import deque

def bfs(graph, start):
    

    return result  # 최종 탐색 경로 반환

# 그래프 인접 리스트
graph = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B', 'F'], 
    'E': ['B', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['F']
}

start_node = 'A'
result = []  # 탐색 경로를 저장할 리스트
# visited = [False] * len(graph.keys())
visited = set()
queue = deque()
queue.append(start_node)
visited.add(start_node)

while queue:
    vertex = queue.popleft()
    result.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor in visited: continue
        queue.append(neighbor)
        visited.add(neighbor)
print("그래프 탐색 경로:", result)  # 탐색
# 경로 출력
