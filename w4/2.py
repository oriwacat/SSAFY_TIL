N = 5
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
total_sum = 0

for i in range(N):
    for j in range(N):
        num_sum = 0

        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0 <= ni < N and 0 <= nj < N:
                num_sum += abs(matrix[i][j] - matrix[ni][nj])
        total_sum += num_sum
print(total_sum)