# i
# 6
# 1
# 2
# 3
# 1
# 1
# 5
# 2 4
# 2 2
# o
# 2
# 1
# 5
# from collections import deque
# n = int(input())
# blocks = [int(input()) for _ in range(n)]
# s1, e1 = map(int, input().split())
# s2, e2 = map(int, input().split())
# blocks = deque(blocks)
# box = []
# box = deque(box)
# for i in range(1,n+1):
#     if s1 <= i <= e1:
#         blocks.popleft()
#     else:
#         box.append(blocks.popleft())
#
# for i in range(1,len(box)+1):
#     if s2 <= i <= e2:
#         box.popleft()
#     else:
#         blocks.append(box.popleft())
#
# print(len(blocks))
# for x in blocks:
#     print(x)