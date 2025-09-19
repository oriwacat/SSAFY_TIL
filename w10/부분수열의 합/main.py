import sys
sys.stdin = open('sample_input.txt')

def subset(idx, num_sum):
    global result
    if num_sum == K:
        result += 1
        return

    if num_sum >= K: return
    if idx == N: return

    subset(idx+1, num_sum + nums[idx])
    subset(idx+1, num_sum)


T = int(input())
for t in range(1, T+1):
    N, K = map(int,input().split())
    nums = list(map(int,input().split()))
    result = 0
    subset(0,0)

    print(f'#{t} {result}')
