import sys
sys.stdin = open('sample_input.txt')
# from collections import deque
# T = int(input())
#
# for t in range(1, T+1):
#     a, b = input().split()
#     A = deque(list(a))
#     B = list(b)
#     cnt = 0
#     while A:
#         button = False  # 활성화 되면 A에서 B만큼 빼기 위한 버튼
#         for i in range(len(B)):
#             if A[i] != B[i]: # 앞에서부터 A B 비교해서 한번이라도 틀리면 버튼 비활성화
#                 button = False
#                 A.popleft()
#                 cnt += 1
#                 break
#             button = True
#         #무사히 통과하면 비교한 부분 전부 같다는 뜻
#         if button:
#             for _ in range(len(B)): # B만큼 A빼기
#                 A.popleft()
#             cnt += 1
#     print(f'#{t} {cnt}')


T = int(input())

for t in range(1, T+1):
    A, B = input().split()
    cnt = 0
    while B in A:
        A = A.replace(B, " ", 1)
        cnt += 1

    print(f'#{t} {len(A)}')