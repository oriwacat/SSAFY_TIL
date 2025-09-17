T = int(input())
for tc in range(1, T + 1):
    # 정점 수, 간선 수, 두 정점 a, b 입력
    v_cnt, e_cnt, a_vertex, b_vertex = map(int, input().split())
    edges = list(map(int, input().split()))

    print(f"#{tc}")
