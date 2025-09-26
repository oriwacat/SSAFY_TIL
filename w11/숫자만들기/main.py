import sys
sys.stdin = open('sample_input.txt')

def dfs(idx, current, plus, minus,multi,div):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return
    num = nums[idx]
    if plus:
        dfs(idx +1, current + num, plus-1, minus, multi, div)
    if minus:
        dfs(idx +1, current - num, plus, minus-1, multi, div)
    if multi:
        dfs(idx+1, current * num, plus,minus,multi-1,div)
    if div:
        if current < 0:
            dfs(idx + 1, -(-current // num), plus, minus, multi, div - 1)
        else:
            dfs(idx + 1, current // num, plus, minus, multi, div - 1)


T= int(input())
for t in range(1, T+1):
    N = int(input())
    ch = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    max_val = -1e9
    min_val = 1e9

    dfs(1,nums[0],ch[0],ch[1],ch[2],ch[3])
    print(f'#{t} {max_val - min_val}')
