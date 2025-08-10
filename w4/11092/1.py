import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
  N = int(input())
  numbers = list(map(int, input().split()))
  

  low = numbers.index(min(numbers))
  max_val = max(numbers)
  high = max([i for i, v in enumerate(numbers) if v == max_val])

  result = high - low
  print(f'#{test_case} {abs(result)}')