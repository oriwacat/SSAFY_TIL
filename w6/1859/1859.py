import sys
sys.stdin = open("input.txt")

T = int(input())

pascal = [
    [0],
    [0, 1, 0],
]

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = -999999999
    cnt = 0
    balance = 0
    for i in range(len(arr) - 1, -1, -1):
        if max_v >= arr[i]:
            balance -= arr[i]
            cnt += 1
        else:
            balance += cnt * max_v
            max_v = arr[i]
            cnt = 0
    balance += cnt * max_v
    print(f"#{t + 1} {balance}")