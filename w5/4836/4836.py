import sys
sys.stdin = open("sample_input.txt")

T = int(input())
N = 10
for test_case in range(1, T+1):
    paint = int(input())
    info = [list(map(int, input().split())) for _ in range(paint)]
    matrix = [[0]*N for _ in range(N)]
print(matrix)





