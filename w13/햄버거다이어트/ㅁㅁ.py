import sys
sys.stdin = open("sample_input.txt")

def dfs(depth, score, cal):
    global result

    if cal > L:
        return

    if depth == N:
        result = max(result, score)
        return

    dfs(depth +1, score + toppings[depth][0], cal + toppings[depth][1])
    dfs(depth + 1, score, cal)

T = int(input())

for t in range(1, T+1):
    N, L = map(int,input().split())
    toppings = [list(map(int,input().split())) for _ in range(N)]
    result = 0

    dfs(0,0,0)
    print(f'#{t} {result}')
