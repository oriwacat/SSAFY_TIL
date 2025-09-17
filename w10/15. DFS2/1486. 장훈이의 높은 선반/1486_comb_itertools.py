import sys
from itertools import combinations
sys.stdin = open("input.txt")


"""
모든 조합들(부분집합)을 구하고, 해당 조합들의 키의 합을 선반 높이와의 차를 구한다. 
그리고 그 차 중에서 가장 작은 값을 결과로 출력한다.

접근방법 1)
모든 조합을 구하고, 키를 합해서, 목표 높이에 도달하는지를 본다. 
"""
T = int(input())
for test_case in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 점원들의 키
    arr = list(map(int, input().split()))

    # 점원들의 키의 합이 B를 넘되, 가장 작은 값을 갱신할 변수
    # min_height = N * 10000
    min_height = float('INF')

    # example: arr = [1,2,3]
    # 입력받은 arr에서 1명을 고르는 사람, 2명, 3명 , ..., N명을 고르는 선택으로 모든 조합을 구해볼거다.
    for r in range(1, N+1):
        # r = 1, 2, 3
        # r=1 => [1], [2], [3]
        # r=2 => [1, 2]= 3, [1, 3]=4, [2, 3]=5
        # r=3 => [1, 2, 3] = 6
        comb_list = combinations(arr, r)
        for comb in comb_list:  # 만들어진 조합들의 키의 합을 구한다. 그리고 그 키의 합의 최소값을 구한다. (조건은 B보다 클 것)
            total_height = sum(comb)

            # 무조건 최소값을 갱신하는 것이 아니고
            if total_height >= B:
                min_height = min(total_height, min_height)

    print(f"#{test_case} {min_height - B}")
