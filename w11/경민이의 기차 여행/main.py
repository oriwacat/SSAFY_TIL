import sys, heapq, math
from collections import defaultdict
sys.stdin = open('sample_input.txt')

def dijkstra(graph, start, N):
    distances = {v: math.inf for v in range(N)}
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if distances[current_vertex] < current_distance: continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(min_heap, [distance, adjacent])

    return distances

T = int(input())

for t in range(1, T+1):
    N , E = map(int,input().split())
    graph = defaultdict(dict)
    for _ in range(E):
        a, b, w = map(int,input().split())
        graph[a][b] = w
    res = dijkstra(graph,0, N)

    if res[N - 1] == math.inf:
        print(f'#{t} impossible')
    else:
        print(f'#{t} {res[N - 1]}')
