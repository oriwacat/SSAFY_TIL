import sys
from collections import deque

# sample_input.txt 파일을 읽어오도록 설정 (제출 시에는 주석 처리)
sys.stdin = open('C:/Users/SSAFY/Desktop/a/SSAFY_TIL/w12/홈 방범 서비스/sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    houses = []
    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                houses.append((r, c))

    max_houses_served = 0

    # K: 서비스 영역의 크기
    # K를 1부터 N+1까지 순회합니다. K가 N+1을 넘어가면 모든 집을 포함할 수 있습니다.
    for k in range(1, N + 2):
        operation_cost = k * k + (k - 1) * (k - 1)

        # (r, c): 서비스 영역의 중심 좌표
        for r in range(N):
            for c in range(N):
                current_houses_served = 0
                # 등록된 집 목록을 순회하며 서비스 영역에 포함되는지 확인
                for hr, hc in houses:
                    # 맨해튼 거리 계산
                    if abs(hr - r) + abs(hc - c) < k:
                        current_houses_served += 1

                # 수익 계산
                revenue = (current_houses_served * M) - operation_cost

                # 수익이 0 이상일 때 (손해를 보지 않을 때)
                if revenue >= 0:
                    # 현재 서비스한 집의 수가 최대값보다 크면 갱신
                    if current_houses_served > max_houses_served:
                        max_houses_served = current_houses_served

    print(f"#{test_case} {max_houses_served}")
