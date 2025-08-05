T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    test_list = list(map(int,input()))

    count = 0
    result = 0

    for i in test_list:
        if i == 1:
            count += 1

        else:
            count = 0

        if count > result:
            result = count

    print(f'#{test_case} {result}') 