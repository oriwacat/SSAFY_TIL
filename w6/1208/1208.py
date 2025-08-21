import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        maxm = max(box)
        a = box.index(maxm)
        box[a] = box[a] - 1

        minm = min(box)
        a = box.index(minm)
        box[a] = box[a] + 1

    result = max(box) - min(box)
    print(f'#{tc} {result}')