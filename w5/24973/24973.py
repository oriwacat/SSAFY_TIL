import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range()