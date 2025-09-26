import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    T = int(input())
    ladder = [list(map(int,input().split()))for _ in range(100)]
    for i in range(100):
        if ladder[99][i] == 2:
            x, y = 99, i

    while x > 0:

        if 0 <= y-1 and ladder[x][y-1] == 1:
            ladder[x][y] = 0
            y-=1
        elif y < 99 and ladder[x][y+1] == 1:
            ladder[x][y] = 0
            y+=1
        elif ladder[x-1][y] == 1:
            ladder[x][y] = 0
            x-=1

    print(f'#{t} {y}')