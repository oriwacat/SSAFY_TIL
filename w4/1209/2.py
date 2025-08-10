#이명재
import sys
sys.stdin = open('input.txt')

for t in range(10):
  test_case = input()
  matrix = [
      list(map(int, input().split())) for _ in range(100)
  ]
  max_v = 0
  for row in matrix: # 가로행 담고
      max_v = max(max_v, sum(row)) # 한줄씩 더해서 max_v랑 비교해서 큰값으로 갱신 반복문 끝나면 가장큰 행값이 담김
  matrix_T = zip(*matrix) # 행과 열을 뒤집는 방법
  
  for column in matrix_T:
      max_v = max(max_v, sum(column)) # max_v랑 가장 큰 열 값비교
  # max_v에는 행과 열 비교값 중 가장 큰 한줄 만 담김      

  diagonal1 = 0
  diagonal2 = 0
  for i in range(100):# for문 두번 하면서 if 할 필요 없네 
      diagonal1 += matrix[i][i]
      diagonal2 += matrix[99-i][i] 
  max_v = max(max_v, diagonal1, diagonal2)

  print(f"#{test_case} {max_v}")