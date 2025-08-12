import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int(input().split))
    station = list(map(int, input().split()))
    # K가 3이면 3만큼 가보고 가장 가까운 데에서 다시 충전
    cnt = 0
    st_n = 0
    x = K
    for i in range(1, N+1):
        if i == 10: # 끝까지 도착하면 종료
            break

        for r in range(x):
            if station[st_n



        x -= 1  # 이동 가능거리
        if x == 0:  # 이동 가능거리 없으면 0 출력
            result = 0


        #
        # if station[st_n] == i:
        #     st_n += 1
        #     x = K
# 나중에 다시해 현재 위치에서 k만큼 이동 했을때 충전소(가장먼) 있으면 거기서 다시이동
