n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
while True:
    trigger = False
    for i in reversed(range(len(numbers))):
        j = i + 1
        while j < len(numbers) and numbers[j] == numbers[i]:
            j += 1
        
        block_len = j - i
        
        if block_len >= m:
            del numbers[i:j]
            trigger = True
            break
    
    if not trigger:
        break


if len(numbers) == 0:
    print(0)
else:
    print(len(numbers))
    for i in numbers:
        print(i)
