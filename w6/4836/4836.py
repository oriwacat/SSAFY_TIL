import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(N)]
    matrix = [[0 for _ in range(10)]for _ in range(10)]
    cnt = 0

    for x in A:
        for i in range(x[0],x[2]+1):
            for j in range(x[1],x[3]+1):
                matrix[i][j] += x[4]

    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                cnt += 1

    print(f'#{t} {cnt}')
