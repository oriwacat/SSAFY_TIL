T = int(input())
count = 1
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int,input().split()))

    
    max_ai = ai[0]
    min_ai = ai[0]
    result = []
    for num in ai: # [477162, 658880, 751280, 927930, 297191]
        if num > max_ai:
            max_ai = num
        if num < min_ai:
            min_ai = num
            
    
    result = max_ai - min_ai
    print(f'#{count} {result}')
    count += 1

            
