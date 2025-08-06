T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    card = list(map(int,input()))
    max_number = 0
    max_count = 0

    for i in range(10):
        count = card.count(i)
        
        if count > max_count:
            max_count = count
            max_number = i
        elif count == max_count and i > max_number:
            max_number = i
        
    print(f"#{test_case} {max_number} {max_count}")