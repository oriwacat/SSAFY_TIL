import sys
sys.stdin = open('sample_input.txt')

def go(idx,num,summ,minm,mul,div):
    global mx
    global mn
    if idx == N:
        mx = max(num, mx)
        mn = min(num, mn)
        return

    if summ > 0:
        go(idx+1, num+nums[idx],summ-1,minm,mul,div)
    if minm > 0:
        go(idx+1, num-nums[idx],summ,minm-1,mul,div)
    if mul > 0:
        go(idx+1, num*nums[idx],summ,minm,mul-1,div)
    if div > 0:
        go(idx+1, int(num/nums[idx]),summ,minm,mul,div-1)



T = int(input())

for t in range(1, T+1):
    N = int(input())
    cal = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    mn = 1e9
    mx = -1e9
    go(1,nums[0],cal[0],cal[1],cal[2],cal[3])
    print(mx-mn)