import sys
sys.stdin = open("sample_input(3).txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    ton = list(map(int, input().split()))