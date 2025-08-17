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
    result = []
    spoint = []
    x = (1, -1, 0, 0)
    y = (0, 0, 1, -1)
    
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == pos:
                spoint.append((i, j))

    for i, j in spoint:
        ii, jj = i, j
        cnt = 1
        
        while True:
            n_ii, n_jj = 0, 0
            n_pos = map_list[ii][jj]

            for k in range(4):
                dx = ii + x[k]
                dy = jj + y[k]
                if 0 <= dx < N and 0 <= dy < N and map_list[dx][dy] < n_pos:
                    n_pos = map_list[dx][dy]
                    n_ii, n_jj = dx, dy
                
            if n_ii == 0:
                break
            ii, jj = n_ii, n_jj
            cnt += 1

        result.append(cnt)
    print(f'#{tc} {max(result)}')