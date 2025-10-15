import sys
sys.stdin = open("sample_input.txt")

def dfs(depth, total_score, total_calorie):
    global result

    if total_calorie > L:
        return

    if depth == N:
        result = max(result, total_score)
        return

    dfs(depth+1, total_score + toppings[depth][0], total_calorie + toppings[depth][1])
    dfs(depth+1, total_score, total_calorie)

T = int(input())

for t in range(1, T+1):
    N, L = map(int,input().split())
    toppings = [list(map(int,input().split())) for _ in range(N)]
    result = 0

    dfs(0,0,0)

    print(f'#{t} {result}')