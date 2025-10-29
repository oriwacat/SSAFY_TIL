def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1


n = 5
parent = [i for i in range(n+1)]
rank = [0] * (n+1)