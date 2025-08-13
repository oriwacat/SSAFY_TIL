import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    a = []
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    for l in range(N):
        for p in range(N):
            a.append(map_list[l][p])
    pos = max(a)
    goal = min(a)
    cnt = 0
    ww = []
    wc = []
    result = []
    box = []

    x = (1, -1, 0, 0)
    y = (0, 0, 1, -1)
    while pos > goal:
        for i in range(N):
            for j in range(N):
                if map_list[i][j] == pos:

        for i in range(N):
            for j in range(N):
                if map_list[i][j] == pos:  # 20

                    for k in range(4):
                        dx = i + x[k]
                        dy = j + y[k]
                        if 0 <= dx < N and 0 <= dy < N:
                            box.append(map_list[dx][dy])
                    pos = min(box)  # 15
                    cnt += 1
        result.append(cnt)
    print(f'#{tc} {max(result)}{ww}')