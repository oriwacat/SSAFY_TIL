import sys
sys.stdin = open('input.txt')
dxy = [[0,1],[0,-1],[1,0],[-1,0]]
T = int(input())
for t in range(T):
    m,n,h = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(n*h)]
    cnt = 0
    # if 0 not in arr:
    #     print(cnt)
    #     continue

    while True:
        box = []
        for r in range(h):
            for i in range(m):
                for j in range(n):
                    if arr[i][j+(r*n)] == 1:
                        for x,y in dxy: #상하좌우 전파
                            nx,ny = i + x, j+(r*n) + y
                            if 0 > nx or nx >= m or 0 > ny or ny >= n + (n*r): continue
                            if not arr[nx][ny]:
                                box.append([nx,ny])
                        if j+(n*r) < n*h: # 윗상자 전파
                            if not arr[i][j+(n*r)]:
                                box.append([i,j+(n*r)])
                        if j-(n*r) >= 0: #아랫상자 전파
                            if not arr[i][j-(n*r)]:
                                box.append([i,j-(n*r)])
        if box:
            cnt += 1
            for xx,xy in box:
                arr[xx][xy] = 1
            box = []
        else:
            break


    print(cnt)