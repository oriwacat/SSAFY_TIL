import sys
sys.stdin = open('input.txt')
import heapq

def prim():
    ans = 0
    min_heap = []
    visited = set()

    heapq.heappush(min_heap, [0, 1])


    while min_heap:
        val, pos = heapq.heappop(min_heap)

        if pos in visited: continue

        visited.add(pos)
        ans += val

        for next_pos, next_val in graph[pos]:
            if type_arr[pos - 1] != type_arr[next_pos - 1] and next_pos not in visited:
                heapq.heappush(min_heap, [next_val, next_pos])

    if len(visited) == n:
        return ans
    else:
        return -1

n, m = map(int, input().split())
type_arr = input().split()
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = { i : [] for i in range(1,n+1)}

for x, y, v in edges:
    graph[x].append((y, v))
    graph[y].append((x, v))

print(graph)
result = prim()


print(result)
