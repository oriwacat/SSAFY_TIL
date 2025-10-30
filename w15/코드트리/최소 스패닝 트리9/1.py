def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return False

    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1
    return True



n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
rank = [0] * (n+1)
parent = [i for i in range(n+1)]
cost = 0
cnt = 0

edges.sort(key=lambda edge: edge[2])

for x,y,v in edges:
    if union(x,y):
        cost += v
        cnt += 1
        if cnt == (n-1):
            break
print(cost)