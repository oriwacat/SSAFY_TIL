# input
#4
#N 3
#E 2
#S 1
#E 2
#output
#4 2
n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x,y = 0,0
for i in range(n):
    if dir[i] == 'N':
        y += dist[i]
    elif dir[i] == 'E':
        x += dist[i]
    elif dir[i] == 'S':
        y -= dist[i]
    elif dir[i] == 'W':
        x -= dist[i]

print(x,y)



# input
# LF
# output
# -1 0

dirs = input()

# Please write your code here.
direction = ((0,1),(1,0),(0,-1),(-1,0))
pos = 0
x,y = 0,0
for i in dirs:
    if i == 'L':
        pos = (pos-1)%4
    elif i == 'R':
        pos = (pos+1)%4
    else:
        dx,dy = direction[pos]
        x,y = x + dx, y + dy
print(x,y)

# input
# 4
# 0 1 0 1
# 0 0 1 1
# 0 1 0 1
# 0 0 1 0
# output
# 4
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
direction = ((0,1),(1,0),(0,-1),(-1,0))
result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k1,k2 in direction:
            dx = i + k1
            dy = j + k2
            if 0 <= dx < n and 0 <= dy < n:
                cnt += grid[dx][dy]
        if cnt >= 3:
            result += 1
print(result)

# input
# 4 4
# 1 2 L
# output
# 1 3

n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
for i in range(t):
    if d == 'L':
        if c > 1:
            c -= 1
        else:
            d = "R"
    elif d == 'R':
        if c < n:
            c += 1
        else:
            d = 'L'
    elif d == 'U':
        if r > 1:
            r -= 1
        else:
            d = "D"
    elif d == 'D':
        if r < n:
            r += 1
        else:
            d = 'U'
print(r,c)