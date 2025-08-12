import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numvers = list(map(int, input().split()))
    s_n = sorted(numvers)
    r_n = sorted(numvers, reverse=True)
    result = []
    for i in range(5):
        result.append(r_n[i])
        result.append(s_n[i])

    print(f'#{test_case} {" ".join(map(str, result))}')



