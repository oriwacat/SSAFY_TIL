import sys
sys.stdin = open('input.txt', 'r')

def runn(matrix, N):
    global cnt
    for i in range(8):
        for j in range(8-N+1):
            aa = matrix[i][j:j+N]
            if aa == aa[::-1]:
                cnt += 1
    return cnt

for t in range(1, 11):
    N = int(input())
    matrix = [list(input()) for _ in range(8)]
    cnt = 0

    result = runn(matrix, N)
    matrix = [list(row) for row in zip(*matrix)]
    result1 = runn(matrix, N)

    print(f'#{t} {result1}')