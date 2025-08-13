import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    pos = cnt = 0
    while pos + K < N:
        next_pos = pos
        for i in range(K, 0, -1):
            if pos + i in chargers:
                next_pos = pos + i
                break
        if next_pos == pos:
            cnt = 0
            break
        pos = next_pos
        cnt += 1
    print(f"#{t} {cnt}")