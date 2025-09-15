# input
# 3
# 1 0 1
# 0 1 0
# 0 1 0
# output
# 4
#
# input
# 5
# 0 0 0 1 1
# 1 0 1 1 1
# 0 1 0 1 0
# 0 1 0 1 0
# 0 0 0 1 1
# output
# 6
# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]
#
# # Please write your code here.
# result = 0
# for i in range(n - 2):
#     for j in range(n - 2):
#         box = 0
#         for x in range(3):
#             for y in range(3):
#                 box += grid[i + x][j + y]
#
#         result = max(result, box)
#
# print(result)

# input
# 3 2
# 1 2 2
# 1 3 4
# 1 2 3
# out put
# 2
# input
# 3 1
# 1 2 3
# 4 5 6
# 7 8 8
# output
# 6
# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]
#
# def happy(grid, n):
#     ttt = 0
#     for i in range(n):
#         cnt = 1
#         ccnt = 0
#         for j in range(1,n):
#             if grid[i][j] == grid[i][j-1]:
#                 cnt += 1
#             else:
#                 ccnt = max(ccnt, cnt)
#                 cnt = 1
#         ccnt = max(ccnt, cnt)
#         if ccnt >= m:
#             ttt += 1
#     return ttt
#
# result = 0
# result += happy(grid, n)
# grid = [list(row) for row in zip(*grid[::-1])]
# result += happy(grid, n)
# print(result)

# inp
# 3 3
# 1 2 3
# 3 2 1
# 3 1 1
# oup
# 8
# inp
# 4 5
# 6 5 4 3 1
# 3 4 4 14 1
# 6 1 3 15 5
# 3 5 1 16 3
# oup
# 45
# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]
# qq = 0
#
# x = [[(0,0),(-1,0),(0,1)],[(0,0),(0,-1),(1,0)],[(0,0),(0,1),(1,0)],[(0,0),(-1,0),(0,-1)],[(0,0),(0,-1),(0,1)],[(0,0),(-1,0),(1,0)]]
# for i in range(n):
#     for j in range(m):
#         for k in x:
#             result = 0
#             for q in k:
#                 a,b = q
#                 dx = i+a
#                 dy = j+b
#                 if 0 <= dx < n and 0 <= dy < m:
#                     result += grid[dx][dy]
#             qq = max(qq, result)
#
# print(qq)