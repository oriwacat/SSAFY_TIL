def comb(arr, n):
    result = []  # 조합을 저장할 리스트

    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]

        for rest in comb(arr[i + 1:], n - 1):  # 조합
            # for rest in comb(arr[:i] + arr[i+1:], n - 1):  # 순열
            # for rest in comb(arr, n - 1):  # 중복순열
            # for rest in comb(arr[i:], n - 1):  # 중복조합
            result.append([elem] + rest)

    return result

i = 2
print(comb([1, 2, 3, 4], i))
#
#
#
# def subsets(nums, index=0, current=None):
#     if current is None:
#         current = []
#
#     # 종료 조건: 끝까지 탐색했으면 출력
#     if index == len(nums):
#         print(current)
#         return
#
#     # 1. 현재 원소를 포함하지 않는 경우
#     subsets(nums, index + 1, current)
#
#     # 2. 현재 원소를 포함하는 경우
#     subsets(nums, index + 1, current + [nums[index]])
#
#
# # 실행
# subsets([1, 2, 3])

# -----------------------------------------------------------

# def comb(arr, n):
#     result = []
#     if n == 1:
#         return [[i] for i in arr]
#
#     for i in range(len(arr)):
#         elem = arr[i]
#         for rest in comb(arr[i + 1:], n - 1):  # 조합
#             result.append([elem] + rest)
#
#     return result
# print(comb([1, 2, 3, 4], 2))


# def perm(arr, n):
#     result = []
#     if n == 1:
#         return [[i] for i in arr]
#
#     for i in range(len(arr)):
#         elem = arr[i]
#         for rest in perm(arr[:i] + arr[i + 1:], n - 1):  # 순열
#             result.append([elem] + rest)
#     return result
# print(perm([1, 2, 3, 4], 2))
#


# def h_perm(arr, n):
#     result = []
#     if n == 1:
#         return [[i] for i in arr]
#
#     for elem in arr:  # 인덱스가 아닌 요소를 직접 순회
#         for rest in h_perm(arr, n - 1):  # 중복순열
#             result.append([elem] + rest)
#     return result
# print(h_perm([1, 2, 3, 4], 2))
#
# def h_comb(arr, n):
#     result = []
#     if n == 1:
#         return [[i] for i in arr]
#
#     for i in range(len(arr)):
#         elem = arr[i]
#         for rest in h_comb(arr[i:], n - 1):  # 중복조합
#             result.append([elem] + rest)
#     return result
# print(h_comb([1, 2, 3, 4], 2))
#

