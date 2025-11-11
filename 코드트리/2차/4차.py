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