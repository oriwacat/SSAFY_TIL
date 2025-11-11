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
