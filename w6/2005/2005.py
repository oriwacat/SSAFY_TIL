import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stacker = []
    print(f'#{tc}')
    for i in range(1,N+1):
        result = []
        stacker2 = []
        stacker.insert(0,int(1))
        for j in range(i):
            x = stacker.pop()
            if stacker2 and stacker :
                result.append(stacker2[-1] + x)
                stacker2.append(x)
            else:
                stacker2.append(x)
                result.append(x)

        print(*result)
        stacker = result

