import sys, time
sys.stdin = open('sample_input.txt')
start = time.time()
time.sleep(1)

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(K)]
    result = 0
    for _ in range(M):
        next_arr = []
        for i in range(len(arr)): #미생물 한번이동
            if arr[i][3] == 1:
                arr[i][0] -= 1
            elif arr[i][3] == 2:
                arr[i][0] += 1
            elif arr[i][3] == 3:
                arr[i][1] -= 1
            elif arr[i][3] == 4:
                arr[i][1] += 1

            if arr[i][0] == 0 or arr[i][0] == (N-1) or arr[i][1] == 0 or arr[i][1] == (N-1): # 살충제 도착
                arr[i][2] = arr[i][2] // 2 # 절반 죽이기
                #방향전환
                if arr[i][3] == 1:
                    arr[i][3] = 2
                elif arr[i][3] == 2:
                    arr[i][3] = 1
                elif arr[i][3] == 3:
                    arr[i][3] = 4
                elif arr[i][3] == 4:
                    arr[i][3] = 3

            if arr[i][2] != 0:
                next_arr.append(arr[i])

        merged = {}
        for x, y, cnt, d in next_arr:
            if (x, y) not in merged:
                merged[(x, y)] = [cnt, d, cnt]  # [총합, 방향, 최대값]
            else:
                merged[(x, y)][0] += cnt
                if cnt > merged[(x, y)][2]:
                    merged[(x, y)][1] = d
                    merged[(x, y)][2] = cnt

        arr = [[x, y, v[0], v[1]] for (x, y), v in merged.items()]
    for i in range(len(arr)):
        result += arr[i][2]

    print(f'#{t} {result}')
print(f'{time.time()-start:.4f}sec')