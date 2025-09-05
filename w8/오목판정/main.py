import sys

sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(str, input())) for _ in range(N)]
    answer = 'NO'

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o':
                if j + 4 < N:
                    for k in range(1, 5):
                        if matrix[i][j + k] != 'o':
                            break
                    else:
                        answer = 'YES'

                if answer == 'NO':
                    if i + 4 < N:
                        for k in range(1, 5):
                            if matrix[i + k][j] != 'o':
                                break
                        else:
                            answer = 'YES'

                if answer == 'NO':
                    if i + 4 < N and j + 4 < N:
                        for k in range(1, 5):
                            if matrix[i + k][j + k] != 'o':
                                break
                        else:
                            answer = 'YES'

                if answer == 'NO':
                    if i + 4 < N and j - 4 >= 0:
                        for k in range(1, 5):
                            if matrix[i + k][j - k] != 'o':
                                break
                        else:
                            answer = 'YES'

            if answer == 'YES':
                break
        if answer == 'YES':
            break
    print(f'#{tc} {answer}')