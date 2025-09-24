import sys
sys.stdin = open('sample_input.txt')

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
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
    p = list(range(n + 1))
    rank = [0] * (n + 1)
    result = []
    for i in range(m):
        sw, x, y = map(int,input().split())
        if not sw:
            union(x, y)
        elif sw:
            # for v in range(1, n + 1):
            #     find_set(v)
            if p[x] == p[y]:
                result.append(1)
            else:
                result.append(0)

    print(f'#{t} {"".join(map(str,result))}')