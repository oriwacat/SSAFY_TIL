high = max([i for i,v in enumerate(numbers) if v == max_v])

for row in matrix: # 가로행 담고
      max_v = max(max_v, sum(row)) # 한줄씩 더해서 max_v랑 비교해서 큰값으로 갱신 반복문 끝나면 가장큰 행값이 담김
  matrix_T = zip(*matrix) # 행과 열을 뒤집는 방법

matrix = [list(map(int,input().split())) for i in range(N)]