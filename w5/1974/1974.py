import sys
sys.stdin = open("input.txt")

T = int(input())
N = 9
for t in range(1, T + 1):
    result = 1
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        if sorted(matrix[i]) != [1,2,3,4,5,6,7,8,9]:
            result = 0
            break
    if result:
        for i in range(3):
            for j in range(3):
                box = []
                for x in range(3*i, 3*i+3):
                    for y in range(3*j, 3*j+3):
                        box.append(matrix[x][y])
                if sorted(box) != [1,2,3,4,5,6,7,8,9]:
                    result = 0
                    break
            if result == 0:
                break
    if result:
        matrix_n = list(zip(*matrix))
        for i in range(N):
            if sorted(matrix_n[i]) != [1,2,3,4,5,6,7,8,9]:
                result = 0
                break

    print(f'#{t} {result}') 

