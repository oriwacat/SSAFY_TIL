import sys
sys.stdin = open('sample_input.txt')

def go(idx,num,plu,miu,mul,div):
    global mn
    global mx
    if idx == N:
        mn = min(num,mn)
        mx = max(num,mx)
        return
    if plu: go(idx+1, num+nums[idx], plu-1, miu, mul, div)
    if miu: go(idx + 1, num - nums[idx], plu , miu- 1, mul, div)
    if mul: go(idx + 1, num * nums[idx], plu , miu, mul- 1, div)
    if div: go(idx + 1, int(num / nums[idx]), plu , miu, mul, div- 1)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    cal = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    mn = 1e9
    mx = -1e9
    go(1,nums[0],cal[0],cal[1],cal[2],cal[3])

    print(mx-mn)