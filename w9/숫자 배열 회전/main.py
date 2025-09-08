import sys
sys.stdin = open('input.txt')

T = int(input())
def role(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

for t in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    result = []
    for i in range(3):
        matrix = role(matrix)
        result.append(matrix)

    print(f'#{t}')
    for i in range(N):
        line = []
        for j in range(3):
            line.append(''.join(map(str, result[j][i])))

        print(' '.join(line))