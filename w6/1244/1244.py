import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    m, c = input().split()
    m = list(map(int, m))
    c = int(c)
    print(m)
