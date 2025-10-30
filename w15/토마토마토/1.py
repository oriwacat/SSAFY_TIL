import sys
sys.stdin = open('input.txt')

m,n,h = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

print(arr)