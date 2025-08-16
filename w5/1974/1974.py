import sys
sys.stdin = open("input.txt")

T = int(input())
N = 9
for t in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N+1):
        if sorted(matrix[i]) != [1,2,3,4,5,6,7,8,9]:
            print(f'#{t} {0}')
            break
    for i in range(3):
        for j in range(3):
           
