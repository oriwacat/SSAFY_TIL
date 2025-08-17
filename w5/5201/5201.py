import sys
sys.stdin = open("sample_input(3).txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    ton = list(map(int, input().split()))
    result = 0
    for t in range(M):
        x = 0
        for w in range(len(weight)):
            if weight[w] <= ton[t] and x < weight[w]:
                x = weight[w]
        result += x
        if x in weight:
            weight.remove(x)
    print(f'#{tc} {result}')