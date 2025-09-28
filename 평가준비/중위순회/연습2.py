import sys
sys.stdin = open('input.txt')

def dfs(i):
    if i <= n:
        dfs(i*2)
        result.append(lst[i])
        dfs(i*2+1)


T = 10
for t in range(1, T+1):
    n = int(input())
    result = []
    lst = [0] * (n+1)
    for i in range(n):
        tlst = input().split()
        idx = int(tlst[0])
        lst[idx] = tlst[1]

    dfs(1)

    print(''.join(result))
