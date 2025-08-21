import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    while True:
        x = M
        answer = 'false'
        for i in range(N):
            for j in range(N):
                if matrix[i][j+x] < N and matrix[i][j+x] == matrix[i][j]:
                    for k in range(M//2):
                        d
                        #하나씩더한 매트릭스랑 하나씩 뺀 매트릭스랑 계속같으면 진행 진행 끝까지하면 answer true
                        #달라졌을 경우 브레이크
                        # 세로로도 하나 더만들면 완성될듯
