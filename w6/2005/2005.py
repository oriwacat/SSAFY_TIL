import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ne = []
    pre = 1
    for i in range(1, N+1):
        result = []
        for j in range(i):
            if ne[j-1] == True:
                reuslt.append(ne[j-1]+ne[j-2])
            else:
                result.append(pre)
        print(result)
        ne = result
