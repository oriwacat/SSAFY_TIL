import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    T = int(input())
    ladder = [list(map(int,input().split()))for _ in range(100)]
    n = 100
    result = {}
    for i in range(n):
        x, y = 0, 0
        temp_ladder = [row[:] for row in ladder]
        if ladder[x][i] == 1:
            y = i
            cnt = 0
            start_point = i
            while x < 99:
                if y - 1 >= 0 and temp_ladder[x][y - 1] == 1:
                    temp_ladder[x][y] = 0
                    y -= 1
                    cnt += 1
                elif y + 1 < n and temp_ladder[x][y + 1] == 1:
                    temp_ladder[x][y] = 0
                    y += 1
                    cnt += 1
                elif temp_ladder[x + 1][y] == 1:
                    temp_ladder[x][y] = 0
                    x += 1
                    cnt += 1
            result[start_point] = cnt
    min_start = min(result, key=lambda k: result[k])
    print(f'#{t} {min_start}')