import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    t = []
    cnt = 0
    time = 0
    for i in range(N):
        s, e = map(int, input().split())
        t.append((s, e))
    
    t.sort(key=lambda x: x[1])
    for s, e in t:
        if s >= time:
            cnt += 1
            time = e
    print(f'#{tc} {cnt}')

