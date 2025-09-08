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
        result.append(role(matrix))
    print(result)