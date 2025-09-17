import sys

sys.stdin = open("input.txt")
"""
부분집합을 구하는 문제다 
DFS(깊이 우선 탐색)
"""
T = int(input())
for test_case in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 각 사람의 키를 입력받아 리스트로 저장
    arr = list(map(int, input().split()))

    min_height = float('INF')

    # idx: 현재 탐색 중인 직원의 인덱스
    # h_sum: 내가 선택해온 직원들의 키의 합
    def dfs(idx, h_sum):  # 재귀적으로 안으로 파고들면서, 점원들의 키의 합 중에서 B를 넘고, 가장 작은 값을 구하는 함수
        global min_height

        # 여태까지 선택한 직원들의 키의 합이.. 이미 우리가 선정한 최소값보다 커졌으면
        # 더 이상 진행할 필요가 없습니다.
        # 가지치기 => 백트래킹 기법
        if h_sum >= min_height:
            return

        # 모든 직원들에 대해서 선택이 끝났다는 거에요.
        if idx == N:
            if h_sum >= B:
                min_height = min(min_height, h_sum)
            return

        # idx에 해당하는 직원을 "선택"한 경우
        dfs(idx+1, h_sum + arr[idx])

        # idx에 해당하는 직원을 "선택하지 않은" 경우
        dfs(idx+1, h_sum)


    """
    재귀함수의 파라미터
    DFS => 스택  => 재귀 
    1. 재귀함수를 종료하기 위한 변수 
    - 점원들을 모두 선택(포함하든/안하든) 했을 때
    - 현재 선택한 점원의 인덱스  
    2. 누적해서 가져가고 싶은 값
    - 우리가 포함한 점원들 키의 합 
    """
    dfs(0, 0)

    print(f"#{test_case}")

