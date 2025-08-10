import sys
sys.stdin = open('input.txt')

for _ in range(10):
  T = int(input().strip())
  def y(num):
    result = []
    for j in range(100):
      y_sum = 0
      for i in range(100):
        y_sum += num[i][j]
      result.append(y_sum)
    return result

  number = [list(map(int, input().split())) for x in range(100)]
  x_matrix = []
  y_matrix = y(number)
  major_diagonal = 0
  anti_diagonal = 0
  for i in range(100):
    x_sum = 0
    for j in range(100):

      if i == j:
        major_diagonal += number[i][j]
      
      if 99-i == j:
        anti_diagonal += number[i][j]
      x_sum += number[i][j]
    x_matrix.append(x_sum)
  a = max(x_matrix)
  b = max(y_matrix)
  maxr = max(a, b, major_diagonal, anti_diagonal)
  print(f'#{T} {maxr}')
  

    