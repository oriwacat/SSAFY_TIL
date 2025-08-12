for t in range(10):
n = int(input())
arr = list(map(int, input().split()))
total = 0
for i in range(2, n-2):
max_v = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
total += max(arr[i] - max_v, 0)
print(f"#{t+1} {total}")