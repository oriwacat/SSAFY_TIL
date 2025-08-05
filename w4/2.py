#선택 정렬
def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
arr = [6, 2, 10, 3, 9, 1]
print(selection_sort(arr))

# 삽입정렬
def insertion_sort(arr):
    n = len(arr)

    for idx in range(1, n):
        for jdx in range(idx, 0, -1):
            if arr[jdx -1] > arr[jdx]:
                arr[jdx-1], arr[jdx] = arr[jdx], arr[jdx-1]
            else:
                break
    return arr

arr = [6, 2, 10, 3, 9, 1]
print(insertion_sort(arr))

# 카운팅 정렬
def counting_sort(arr, max_value):
    n = len(arr)

    count_arr = [0] * (max_value + 1)

    for num in arr:
        count_arr[num] += 1
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    
    result = [0] * n

    for i in range(n-1, -1, -1):
        val = arr[i]

        result[count_arr[val] -1] = val
        count_arr[val] -= 1
    
    return result

arr = [6, 2, 10, 3, 9, 1]
result = counting_sort(arr, 10)
print(result)