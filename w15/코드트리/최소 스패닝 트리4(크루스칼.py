import sys
sys.stdin = open('input.txt')
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
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


# 입력
n, m = map(int, input().split())
types = input().split()
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    # 서로 다른 타입끼리만 간선 추가
    if types[u-1] != types[v-1]:
        edges.append((w, u, v))

edges.sort(key= lambda x: x[0])

# 초기화
parent = [i for i in range(n+1)]
rank = [0] * (n+1)
print(parent, rank)
total_cost = 0
cnt = 0

for w, u, v in edges:
    if union(u, v):
        total_cost += w
        cnt += 1
        if cnt == n - 1:
            break

if cnt == n - 1:
    print(total_cost)
else:
    print(-1)
