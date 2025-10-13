def kruskal(n, edges):
    parent = list(range(n + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x_root, y_root = find(x), find(y)
        if x_root == y_root:
            return False
        parent[y_root] = x_root
        return True

    edges.sort(key=lambda x: x[2])  # 비용 기준 정렬
    total_cost = 0
    count = 0

    for x, y, cost in edges:
        if union(x, y):
            total_cost += cost
            count += 1
            if count == n - 1:
                break

    return total_cost if count == n - 1 else -1


def solve_all():
    T = int(input())
    for t in range(1, T + 1):
        N, M = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(M)]

        result = kruskal(N, edges)
        print(f"#{t} {result}")


if __name__ == "__main__":
    solve_all()