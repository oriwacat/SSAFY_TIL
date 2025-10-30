import sys
sys.stdin = open('input.txt')

T = int(input())

for tm in range(1,T+1): # 먼지 확산과 돌풍 따로 구현
    n,m,t = map(int,input().split())
