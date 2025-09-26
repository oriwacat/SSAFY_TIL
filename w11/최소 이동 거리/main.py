import sys, heapq, math
from collections import defaultdict
sys.stdin = open('sample_input.txt')


def dijkstra(graph, start):
    distances = {v: math.inf for v in range(N+1)}
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        c_distance, c_vertex = heapq.heappop(min_heap)
        # print(c_distance, c_vertex, '@@@@@@@@@')
        if distances[c_vertex] < c_distance: continue
        for adjacent, weight in graph[c_vertex].items():
            distance = c_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(min_heap, [distance, adjacent])
    return distances[N]

T = int(input())
for t in range(1, T+1):
    N, E = map(int,input().split())
    graph = defaultdict(dict)
    for _ in range(E):
        a, b, w = map(int, input().split())
        graph[a][b] = w

    start_v = 0
    result = dijkstra(graph, start_v)
    print(f'#{t} {result}')
