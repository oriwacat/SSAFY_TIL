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