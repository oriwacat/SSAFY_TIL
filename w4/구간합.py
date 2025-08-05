T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    sm_list = list(map(int,input().split()))

    max_sum = 0
    min_sum = sum(sm_list[0:M])
    
    for i in range(N - M + 1):
        sum_list = sum(sm_list[i:i+M])
        if max_sum < sum_list:
            max_sum = sum_list
        
        elif min_sum > sum_list:
            min_sum = sum_list
    
    result = max_sum - min_sum
    
    print(f'#{test_case} {result}') 