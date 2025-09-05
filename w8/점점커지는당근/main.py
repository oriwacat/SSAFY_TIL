import sys
sys.stdin = open('carrot_sample_in.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    result = 0
    cnt = 1
    for i in range(N-1):
        if carrot[i] < carrot[i+1]:
            cnt +=1
        else:
            result = max(result, cnt)
            cnt = 1
    result = max(result, cnt)
    print(f'#{t} {result}')
