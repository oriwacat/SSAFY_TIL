def sum_subset(depth, num_sum, current_subset):
    global result
    global aa

    # 합계가 10을 초과하면 더 이상 탐색할 필요가 없습니다.
    if num_sum > 10:
        return

    if depth == N:
        if num_sum == 10:
            result += 1
            # 찾은 부분집합의 복사본을 추가합니다.
            aa.append(current_subset)
        return

    # 현재 원소를 포함하는 경우
    sum_subset(depth + 1, num_sum + arr[depth], current_subset + [arr[depth]])

    # 현재 원소를 포함하지 않는 경우
    sum_subset(depth + 1, num_sum, current_subset)


N = 10
result = 0
aa = []
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_subset(0, 0, [])

print(f"합계가 10인 부분집합의 개수: {result}")
print("부분집합 목록:")
for subset in aa:
    print(subset)
