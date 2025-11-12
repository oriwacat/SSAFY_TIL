폭탄

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

def explode_once(numbers):
    nxt = []
    i = 0
    exploded = False  # 터졌는지 체크

    while i < len(numbers):
        j = i
        # 같은 숫자가 몇 개 연속인지 계산
        while j < len(numbers) and numbers[j] == numbers[i]:
            j += 1
        count = j - i

        if count < m:  # 폭발 조건 미만이면 그대로 유지
            nxt.extend(numbers[i:j])
        else:           # 폭발 조건이면 제거
            exploded = True
        i = j  # 다음 구간으로 이동

    return nxt, exploded


# 반복적으로 폭발시키기
while True:
    nxt_numbers, exploded = explode_once(numbers)
    if not exploded:   # 더 이상 터질 게 없으면 종료
        break
    numbers = nxt_numbers

# 결과 출력
print(len(numbers))
for x in numbers:
    print(x)
-------------------------------------------------

폭탄 강사님

# n: 처음 주어지는 폭탄의 개수
# m: m개 이상 연속된 폭탄이 터진다.

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

tmp = []
for i in range(len(numbers) - 1, -1, -1):
    tmp.append(numbers[i])

numbers = tmp[::]


def can_explode(arr):
    if len(arr) <= 0:
        return False

    num = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if numbers[i] == num:
            cnt += 1
        else:
            if cnt >= m and num != 0:
                return True

            cnt = 1
            num = arr[i]

    if cnt >= m and num != 0:
        return True

    return False


def explode(arr):
    tmp = arr[::]

    num = tmp[0]
    cnt = 1

    for i in range(1, len(tmp)):
        # 값이 달라지는 순간이라면
        if tmp[i] != num:
            # 몇번 반복됐는지 파악해서
            # m번 이상 반복됐다면
            if cnt >= m:
                # 앞의 cnt개 만큼을 터뜨린다.
                for j in range(i - cnt, i):
                    tmp[j] = 0

            # 변수 초기화
            cnt = 1
            num = tmp[i]

        else:
            cnt += 1

    if cnt >= m:
        for j in range(i - cnt, len(tmp)):
            tmp[j] = 0

    res = []

    idx = 0
    for i in range(len(tmp)):
        if tmp[i] != 0:
            res.append(tmp[i])

    return res


def print_result(numbers):
    cnt = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            cnt += 1
        else:
            break

    print(cnt)

    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] == 0:
            continue

        print(numbers[i])


# 계속 반복하면서:
#     터질 수 있나? => 터질 수 있으면 터뜨린다.
#     터질 수 없다? => 반복문 탈출

while True:
    if can_explode(numbers):
        numbers = explode(numbers)
    else:
        break

print_result(numbers)

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) - 1 for _ in range(m)]  # 입력이 1-based라면 -1 처리
dxy = [(1,0),(0,1),(-1,0),(0,-1)]

for c in commands:             # 각 명령(열)마다
    # 해당 열에서 위에서부터 내려오며 첫 폭탄을 터뜨림
    for j in range(n):
        if grid[j][c] > 0:
            power = grid[j][c]
            grid[j][c] = 0     # 자기 자신은 무조건 터짐

            if power > 1:
                for dx, dy in dxy:
                    for p in range(1, power):   # 거리 1 ~ power-1
                        nx, ny = j + dx*p, c + dy*p
                        if 0 <= nx < n and 0 <= ny < n:
                            grid[nx][ny] = 0
            break  # 한 열에서 첫 번째 폭탄만 터뜨리고 다음 명령으로

    # --- 여기에 '중력' 적용: 각 열의 숫자들이 아래로 내려가게 함 ---
    for col in range(n):
        stack = []
        # 위에서 아래로 비제로 값을 수집
        for row in range(n):
            if grid[row][col] != 0:
                stack.append(grid[row][col])
            grid[row][col] = 0  # 일단 칸을 비운다

        # 바닥(n-1)부터 채우기 (원래 순서 유지)
        r = n - 1
        while stack:
            grid[r][col] = stack.pop()  # 마지막 원소가 바닥으로
            r -= 1

# 결과 출력
for row in grid:
    print(*row)