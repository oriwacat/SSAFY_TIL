import sys
sys.stdin = open('s_input.txt')

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1
T = int(input())

for t in range(1, T+1):
    n, m = map(int,input().split())
    p = list(range(n+1))
    rank = [0] * (n+1)

    for i in range(m):
        x, y = map(int,input().split())
        union(x,y)

    result = set()
    for v in range(1, n+1):
        result.add(find_set(v))
    print(f'#{t} {len(result)}')