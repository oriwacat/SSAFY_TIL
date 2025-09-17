# 트리의 인접 리스트 표현
tree = {'A': ['B', 'C', 'D'], 
        'B': ['E', 'F'], 
        'D': ['G', 'H', 'I']}

def dfs(tree, node):
    
    # 전위 순회 (부모 -> 왼쪽 -> 오른쪽)
    print(node)


    # 자식 노드가 없는 경우에는 탐색 종료
    if node not in tree: 
        return
    
    # 이웃 노드들을 순서대로 다시 탐색
    for child in tree[node]:
        dfs(tree, child)

    # 후위 순회 ( 왼쪽 -> 오른쪽 -> 부모 )
    # print(node)

# 루트 노드 'A'부터 DFS 탐색 시작
dfs(tree, 'A')