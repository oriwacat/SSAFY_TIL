
def dfs(graph, start, visited, result):
    visited.add(start)  
    result.append(start) 
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)  

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
visited = set() 
result = []  

dfs(graph, start_vertex, visited, result) 

print(' '.join(result))
