import sys
sys.stdin = open('input.txt')

def dfs(n):
    if n > N:
        return

    dfs(n*2)
    ans.append(lst[n])
    dfs(n*2+1)


T = 10
for t in range(1, T+1):
    N = int(input())

    lst = [0] * (N+1)
    for _ in range(N):
        tlst = input().split()
        idx = int(tlst[0])
        lst[idx] = tlst[1]

    ans = []
    dfs(1)

    print(''.join(ans))