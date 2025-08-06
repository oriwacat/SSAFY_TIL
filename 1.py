T = int(input())


for tast_case in range(T):
  N, M = map(int, input().split())
  balloons = []
  result = 0
  
  for i in range(N):
    balloons.append(list(map(int, input().split())))
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  for i in range(N):
    for j in range(M):
      sum = 0
      for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]

        if 0 <= ni < N and 0 <= nj < M:
          sum += balloons[ni][nj]
      if sum > result:
        result = sum

  print(f'#{tast_case} {result}')

