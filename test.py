N=3
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,10]
]

# 각 행의 합을 result에 넣을 건데
# 조건 : 홀수 행만 넣으세요 (인덱스로치면 0, 2, 4, ... ) , 행 ( 1, 3, 5, ... )
# 원하는 결과 : [6, 25]
result = []
for i in range(N):
    add_num = 0
    for j in range(N):
        add_num += matrix[i][j]
    if i % 2 == 0:
        result.append(add_num)
    print(sum(result))