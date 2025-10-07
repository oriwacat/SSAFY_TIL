import sys
sys.stdin = open('input.txt')

def dfs(gg,n):
    global result
    if n == change:
        result = max(result, int("".join(map(str, gg))))
        return

    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            gg[i],gg[j] = gg[j],gg[i]

            check = int("".join(map(str, gg)))
            if (n, check) not in visited:
                dfs(gg,n + 1)
                visited.append((n, check))

            gg[i], gg[j] = gg[j], gg[i]




T = int(input())

for t in range(1,T+1):
    a,change = map(int,input().split())
    lst = [int(i) for i in str(a)]
    L = len(lst)
    visited = []
    result = 0
    dfs(lst,0)
    print(f'#{t} {result}')