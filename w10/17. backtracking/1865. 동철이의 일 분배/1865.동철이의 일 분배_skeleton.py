import sys
sys.stdin = open('1865_input.txt', "r")


def search():
    pass

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 함수 작성 필요
    search()

    print(f'#{tc}')
