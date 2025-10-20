import sys
sys.stdin = open('sample_input.txt')
# 내코드 실행시간 1313
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
    # print(next_arr)
        next_arr.sort(key= lambda x: x[2], reverse=True)
        for i in range(len(next_arr)): #같은 좌표 군집 합치기
            for j in range(i+1,len(next_arr)):
                if next_arr[i][0] == next_arr[j][0] and next_arr[i][1] == next_arr[j][1]:
                    next_arr[i][2] += next_arr[j][2]
                    next_arr[j][2] = 0

        arr = [a for a in next_arr if a[2] != 0]
    for i in range(len(arr)):
        result += arr[i][2]

    print(f'#{t} {result}')

