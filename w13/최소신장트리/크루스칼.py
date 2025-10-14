import sys
sys.stdin = open('algo1_sample_in.txt')

# Union-Find (Disjoint Set) ----------------------
def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        parent[py] = px
        return True
    return False

T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    # 간선을 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    parent = list(range(n+1))
    total_weight = 0
    edge_count = 0

    for x, y, w in edges:
        # 사이클이 생기지 않으면 연결
        if union(x, y):
            total_weight += w
            edge_count += 1
        # MST 완성 조건: 간선 수 = 정점 수 - 1
        if edge_count == n - 1:
            break

    # MST가 완성되지 않은 경우 (-1 출력)
    if edge_count != n - 1:
        print(f'#{t} {-1}')
    else:
        print(f'#{t} {total_weight}')
