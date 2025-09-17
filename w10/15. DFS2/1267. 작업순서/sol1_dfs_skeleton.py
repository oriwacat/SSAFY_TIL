import sys
sys.stdin = open('sample_input.txt')
from collections import defaultdict


T = 10
for tc in range(1, T + 1):
    v_cnt, e_cnt = map(int, input().split())

    print(f"#{tc}", )
