import sys
sys.stdin = open("carrot_sample_in.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 0
    pos = 0
    result = 0
    for i in range(N):
        if C[i] > pos:
            pos = C[i]
            cnt += 1
        else:
            pos = C[i]
            if result < cnt:
                result = cnt
            cnt = 1
    
    print(f'#{tc} {max(cnt, result)}')