n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
qq = 0

x = [[(0,0),(-1,0),(0,1)],[(0,0),(0,-1),(1,0)],[(0,0),(0,1),(1,0)],[(0,0),(-1,0),(0,-1)],[(0,0),(0,-1),(0,1)],[(0,0),(-1,0),(1,0)]]
for i in range(n):
    for j in range(m):
        for k in x:
            result = 0
            for q in k:
                a,b = q
                dx = i+a
                dy = j+b
                if 0 <= dx < n and 0 <= dy < m:
                    result += grid[dx][dy]
            qq = max(qq, result)

print(qq)
