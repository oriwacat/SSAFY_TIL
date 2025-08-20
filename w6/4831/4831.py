import sys
sys.stdin = open("sample_input.txt")


T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    temp = 0
    cnt = 0

    for i in range(N+1):
        result = False

        if temp != i: # 현재위치가 i 랑 같을때만 아래 코드 실행
            continue

        if N <= K + temp: # 현재위치 + k = 도착지점일 경우 종료
            break

        for j in range(i + 1, K + i + 1):
            if j in station:
                temp = j
                result = True

        if not result:
            cnt = 0
            break
        cnt += 1
    print(f'#{tc} {cnt}')

# for문으로 노선 길이만큼 진행 하면서 처음앤 한번 코드 진행해주고 현재 위치를 temp에 저장해서 i가 temp랑 일치될 때만
# 코드를 다시 진행한다 다시 현재위치를 갱신하고 카운트를 하나씩 올린다