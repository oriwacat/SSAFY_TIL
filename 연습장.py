T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    min_height = float('INF')

    def dfs(idx, h_sum):
        global min_height

        if h_sum >= min_height:
            return

        if idx == N:
            if h_sum >= B:
                min_height = min(min_height, h_sum)
            return

        dfs(idx+1, h_sum + arr[idx])
        dfs(idx+1, h_sum)

    dfs()

    print()