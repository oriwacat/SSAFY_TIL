import sys
sys.stdin = open('sample_input.txt')
T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    p = [i for i in range(V + 1)]
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])


    def find_set(x):
        if p[x] != x:
            p[x] = find_set(p[x])
        return p[x]


    def union_set(a, b):
        pa = find_set(a)
        pb = find_set(b)
        if pa > pb:
            p[pa] = pb
        else:
            p[pb] = pa


    total = 0
    for edge in edges:
        n1, n2, w = edge
        root_n1 = find_set(n1)
        root_n2 = find_set(n2)
        if root_n1 != root_n2:
            union_set(n1, n2)
            total += w
    print(f'#{t + 1}', total)