import sys
from itertools import combinations

sys.stdin = open("1486_input.txt")


T = int(input())
for test_case in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 각 사람의 키를 입력받아 리스트로 저장
    heights = list(map(int, input().split()))

    print(f"#{test_case}")

