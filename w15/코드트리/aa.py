n, m = map(int, input().split())
a, b = map(int, input().split())
graph = {i : {} for i in range(1, n+1)}

for _ in range(m):
    from_V, to_v, satistaction = map(int, input().split())
    graph[from_V][to_v] = satistaction
    graph[to_v][from_V] = satistaction

visited = set()

print(graph[1].items())