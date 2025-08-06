N = int(input())

l3i6s9t = []
for i in range(N):
    count = 0
    x = i
    if x >= 300:
        count += 1
        x = x % 300
        if x >= 30:
            count += 1
            x = x % 30
            if x >= 3:
                count += 1
                
        l3i6s9t.append('-' * count)
        pass


    l3i6s9t.append(i) 