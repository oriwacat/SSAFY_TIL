import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = []
    if N > M:
        for i in range(N - M + 1):
            sum = 0
            for j in range(M):
                sum += A[i+j] * B[j]
            result.append(sum)    
            
    elif M > N:
        for i in range(M - N + 1):
            sum = 0
            for j in range(N):
                sum += B[i+j] * A[j]
            result.append(sum)  

    elif N == M:
        sum = 0
        for i in range(N):
            sum += A[i] * B[i]
        result.append(sum)
        
    print(f'#{tc} {max(result)}')