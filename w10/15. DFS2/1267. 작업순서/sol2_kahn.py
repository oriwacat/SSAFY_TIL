from collections import defaultdict, deque


T = 10
for tc in range(1, T + 1):
    v_cnt, e_cnt = map(int, input().split())
    graph = defaultdict(list)

    # 그래프 구성
    edges = list(map(int, input().split()))
    for i in range(e_cnt):
        graph[edges[2 * i]].append(edges[2 * i + 1])

    # 모든 노드들의 진입차수를 구해야한다.
    # 진입차수를 저장할 변수를 만들자.
    in_degree = [0] * (v_cnt + 1)

    """
    graph = {"시작정점" : 도착 정점 리스트, ..., }
    시작 정점을 기준으로 인접한 정점을 for문을 돌면서, 시작 정점을 인덱스로한 공간에 +1 씩 해준다. 
    """
    # node는 시작 정점
    for node in graph:
        # node(시작 정점)의 인접한 노드를 순회하면서, 진입 차수를 +1씩 해준다.
        for neighbor in graph[node]:
            in_degree[node] += 1

    # 진입 차수가 0인 노드들을 큐에 추가한다.
    # 진입 차수가 0 => 의존성이 없다.. 즉 먼저 실행되어야 할 노드들이다.
    # DAG 그래프는 반드시 진입 차수가 0인 노드가 존재한다.
    queue = deque()
    for i in range(1, v_cnt + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    # 큐가 빌 때까지 아래 과정을 실행
    # 1. 큐에 있는 값을 꺼낸다.
    # 2. 큐와 연결된 노드들의 진입차수를 1씩 빼준다.
    # 3. 뺀 진입차수가 0이 된 노드들은 다시 큐에 집어넣는다.
    while queue:
        node = queue.popleft()
        result.append(node)

        # 인접한 노드를 순회하면서, 인접한 노드들의 진입차수를 1씩 빼준다.
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 싸이클 탐지 코드를 추가해야 한다.
    """
    1번 케이스) 아예 시작부터 진입차수가 0인 애들이 없어서, 시작조차 못하는 케이스 
    """
    if len(result) != v_cnt:
        print("싸이클 찾았습니다!")
    else:
        print(f"#{tc} ", *result)
