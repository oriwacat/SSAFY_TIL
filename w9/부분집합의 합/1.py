def a(arr, n):
    result = []
    if n == 1:
        return [[i]for i in arr]

    for i in range(len(arr)):
        elem = arr[i]

        for rest in a(arr[i+1:],n-1):
            result.append([elem] + rest)
    return result

T = int(input())
for t in range(1, T+1):
    resul = 0
    d = []
    N, K = map(int,input().split())
    for i in range(13):
        d.append( a([1,2,3,4,5,6,7,8,9,10,11,12],i))

    for ss in d:
        for tt in ss:
            sum = 0
            if len(tt) == N:
                for kk in tt:
                    sum += kk
                if sum == K:
                    resul += 1

    print(f'#{t} {resul}')

