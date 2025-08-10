import sys
sys.stdin = open("input.txt")



for r in range(1, 10):
    T = input()

    num = list(map(int, input().split()))
    test_list = []
    sum_num1 = 0
    sum_num2 = 0
    y = 0
    for i in range(10):
        row = []
        for j in range(10):
            row.append(num[(i*10)+j])
        test_list.append(row)

    for i in range(10):
        x = sum(test_list[i])
        for j in range(10):
            y += test_list[i][j]
            if i == j:
                sum_num1 += test_list[i][j]

            elif 9-i == j:
                sum_num2 += test_list[i][j]
            else:
                pass

        if sum_num1 > x:
            sum_num1 = x
        elif sum_num2 > y:
            sum_num2 = y
    print(f'#{T} {max(sum_num1, sum_num2)}')

