import sys
sys.stdin = open("in.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    result = []
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if box[i] > box[j]:
                cnt += 1
        result.append(cnt)

    print(f'#{test_case} {max(result)}')