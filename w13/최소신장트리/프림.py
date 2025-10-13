import sys
sys.stdin = open('algo1_sample_in.txt')
import heapq
from collections import defaultdict

def prim(n, edges):
    graph = defaultdict(list)
    for u, v, cost in edges:
        graph[u].append((cost, v))
        graph[v].append((cost, u))

    visited = [False] * (n + 1)
    min_heap = [(0, 1)]  # (비용, 시작점)
    total_cost = 0
    connected = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_cost += cost
        connected += 1
        for next_cost, neighbor in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (next_cost, neighbor))

    return total_cost if connected == n else -1


def solve_all():
    T = int(input())
    for t in range(1, T + 1):
        N, M = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(M)]

        result = prim(N, edges)
        print(f"#{t} {result}")


if __name__ == "__main__":
    solve_all()