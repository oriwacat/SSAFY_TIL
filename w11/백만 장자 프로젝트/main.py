import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    day = int(input())
    price = list(map(int,input().split()))
    x = price[day-1]
    result = 0
    for i in range(day-1,-1,-1):
        if x <= price[i]:
            x = price[i]
        else:
            result += x - price[i]

    print(f'#{t} {result}')
