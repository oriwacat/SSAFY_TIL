import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    answer = []
    a = 0
    while True:

        for i in range(N):
            for j in range(N - M +1):
                for k in range(M // 2):
                    if matrix[i][j + M - 1 - k] == matrix[i][j + k]:
                        # answer.insert(k, matrix[i][j+M-1-k])
                        a = 1
                    else:
                        answer = []
                        a = 0
                        break
                if a == 1:
                    for l in range(M):
                        answer.append(matrix[i][j+l])
                if len(answer) == M:
                    break
            if len(answer) == M:
                break
        if len(answer) == M:
            break
        matrix = [list(row) for row in zip(*matrix)]
    t = ''.join(answer)
    print(f'#{tc} {t}' )
                        #하나씩더한 매트릭스랑 하나씩 뺀 매트릭스랑 계속같으면 진행 진행 끝까지하면 answer true
                        #달라졌을 경우 브레이크


# =================================================
# 아래는 효율성과 가독성을 개선한 코드 제안입니다.
# =================================================

def find_palindrome_in_rows(matrix, N, M):
    for i in range(N):
        for j in range(N - M + 1):
            candidate = matrix[i][j:j+M]
            if candidate == candidate[::-1]:
                return "".join(candidate)
    return None

# import sys
# sys.stdin = open("sample_input.txt")

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     char_matrix = [list(input()) for _ in range(N)]
    
#     result = find_palindrome_in_rows(char_matrix, N, M)
    
#     if result is None:
#         transposed_matrix = [list(row) for row in zip(*char_matrix)]
#         result = find_palindrome_in_rows(transposed_matrix, N, M)
        
#     print(f'#{tc} {result}')
