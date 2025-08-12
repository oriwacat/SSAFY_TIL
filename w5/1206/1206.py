import sys
sys.stdin = open("sample_input.txt")

T = 10

for test_case in range(1, T+1):
    R = int(input())
    N = list(map(int, input().split()))
    x = (-1, -2, 1, 2)
    result = 0
    for i in range(R): #건물 개수만큼 반복
        diff = 1000
        for k in range(4): # 좌우 2개 씩 비교 위해 4번 반복
            di = i + x[k] # 좌우 2개 좌표 정의
            if 0 <= di < R:
                if N[i] > N[di]: # i위치 건물과 i좌우 건물들 비교 i가 높을때 다음
                    if diff > N[i] - N[di]: # 높이차이가 적은 값으로 갱신
                        diff = N[i] - N[di]
                else:
                    diff = 0
                    break
        result += diff
    print(f'#{test_case} {result}')