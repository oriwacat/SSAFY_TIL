from collections import defaultdict, deque


T = 10
for tc in range(1, T + 1):
    v_cnt, e_cnt = map(int, input().split())
    graph = defaultdict(list)

    # 그래프 구성
    edges = list(map(int, input().split()))
    for i in range(e_cnt):
        graph[edges[2 * i]].append(edges[2 * i + 1])

    print(f"#{tc}")
