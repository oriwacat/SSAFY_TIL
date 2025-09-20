n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
trigger = True
while True:

    for i in range(len(numbers)):
        trigger = True
        for j in range(1,m):
            if i+j < n and numbers[i] != numbers[i+j]:
                trigger = False
        if trigger:
            for _ in range(m):
                numbers.pop(i)

            break

    if len(numbers) == 0:
        break
    if not trigger:
        break


if len(numbers) == 0:
    print(0)
else:
    for i in numbers:
        print(i)
