n, m = map(int, input().split())
# query = [list(map(int, input().split())) for _ in range(m)]
#
# uf = [0] * (n+1)
#
# for i in range(n):
#     uf[i] = i
#
# def find(x):
#     if uf[x] == x:
#         return x
#
#     uf[x] = find(uf[x])
#     return uf[x]
#
# def union(x, y):
#     uf[find(x)] = find(y)
#
# for q in query:
#     method = q[0]
#     a = q[1]
#     b = q[2]
#
#     if method == 0:
#         union(a,b)
#     else:
#         root_a = find(a)
#         root_b = find(b)
#         if root_a == root_b:
#             print(1)
#         else:
#             print(0)


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

uf = [0] * (n+1)

for i in range(n+1):
    uf[i] = i

def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    uf[find(x)] = find(y)

for i in range(m):
    src = edges[i][0]
    dst = edges[i][1]

    if find(src) == find(dst):
        print(i+1)
        exit()

    union(src, dst)
print('happy')