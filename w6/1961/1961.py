import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for i in range(3):
        result.append(list(zip(*matrix[::-1])))

    print(''.join(map(str,result)))