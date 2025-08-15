def man(val):
    global switch
    num = next(iter(i[val].values()))
    for jdx in range(1, N+1):
        if jdx % num == 0:
            switch[jdx-1] = 1 - switch[jdx-1]
    
def woman(val, c):
    global switch
    x = next(iter(i[val].values())) -1
    if x-c >= 0 and x+c < N and switch[x-c] == switch[x+c]:
        switch[x-c] = 1 - switch[x-c]
        switch[x+c] = 1 - switch[x+c]
        c += 1
        woman(val, c)
    else:
        switch[x] = 1 - switch[x]


N = int(input())
switch = list(map(int, input().split()))
students = int(input())
i = {}
c = 1
for idx in range(students):
    x, y = map(int, input().split())
    i[idx] = {x : y}

for idx in range(students):
    key = next(iter(i[idx]))  
    if key == 1:
        man(idx)
    elif key == 2:
        woman(idx, c)

for i in range(N):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()

    