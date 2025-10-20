from collections import defaultdict
 
test_case = int(input())
for tc in range(1, test_case+1):
    N, M, K = map(int, input().split())
    micro = []
 
    turn = {1: 2, 2: 1, 3: 4, 4: 3}
 
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
 
    for i in range(K):
        row, col, size, direct = map(int, input().split())
        micro.append([row, col, size, direct])
 
    for time in range(M):
 
        next_pos = defaultdict(list)
 
        for r, c, size, direct in micro:
            nx, ny = r + dx[direct], c + dy[direct]
 
            if nx == 0 or ny == 0 or nx == N-1 or ny == N-1:
                size //= 2
                direct = turn[direct]
 
            if size > 0:
                next_pos[(nx, ny)].append([size, direct])
 
        new_micro = []
 
        for (r, c), colonies in next_pos.items():
            if len(colonies) == 1:
                size, direct = colonies[0]
                new_micro.append([r, c, size, direct])
            else:
                max_size_colony = max(colonies, key = lambda x: x[0])
                direction = max_size_colony[1]
 
                total_size = sum(colony[0] for colony in colonies)
 
                new_micro.append([r, c, total_size, direction])
 
        micro = new_micro
 
    result = sum(colony[2] for colony in micro)
 
    print(f'#{tc} {result}')