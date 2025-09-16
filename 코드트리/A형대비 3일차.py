# i
# 3 1
# 1 2 3
# 6 5 1
# o
# 1 1 2
# 3 6 5
# i
# 3 3
# 1 2 3
# 6 5 1
# o
# 6 5 1
# 1 2 3
# from collections import deque
# n, t = map(int, input().split())
# u = list(map(int, input().split()))
# d = list(map(int, input().split()))
# u = deque(u)
# d = deque(d)
# for _ in range(t):
#     d.appendleft(u.pop())
#     u.appendleft(d.pop())
#
# print(*u)
# print(*d)


# i
# 3 1
# 1 2 4
# 5 9 3
# 6 5 1
#
# o
# 1 1 2
# 4 5 9
# 3 6 5
# n, t = map(int, input().split())
#
# l = list(map(int, input().split()))
# r = list(map(int, input().split()))
# d = list(map(int, input().split()))
#
#
# for _ in range(t):
#     temp_l = l[n-1]
#     temp_r = r[n-1]
#     temp_d = d[n-1]
#     for i in range(n-1,0,-1):
#         l[i] = l[i-1]
#         r[i] = r[i-1]
#         d[i] = d[i-1]
#     l[0] = temp_d
#     r[0] = temp_l
#     d[0] = temp_r
# print(*l)
# print(*r)
# print(*d)

