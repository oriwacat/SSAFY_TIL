import math

# 유니온 파인드(Disjoint Set)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 입력
n, m = map(int, input().split())

x = []
y = []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

edges = [tuple(map(int, input().split())) for _ in range(m)]

# 부모 테이블 초기화
parent = [i for i in range(n + 1)]

# 이미 연결된 간선 미리 union
for a, b in edges:
    union(a, b)

# 모든 점쌍의 거리 계산
dist_edges = []
for i in range(n):
    for j in range(i + 1, n):
        dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
        dist_edges.append((dist, i + 1, j + 1))

# 거리 기준 정렬
dist_edges.sort()

# Kruskal 수행
result = 0.0
for cost, a, b in dist_edges:
    if find(a) != find(b):
        union(a, b)
        result += cost

# 결과 출력 (소수 둘째 자리까지)
print(f"{result:.2f}")
