import sys
sys.stdin = open("sample_in.txt")

T = int(input())
for t in range(1, T + 1):
  N, M = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(N)]
  result = 0
  for i in range(N):
    cnt = 0
    for j in range(M):
      if matrix[i][j]:
        cnt += 1
        continue
      result = max(result, cnt)
      cnt = 0
    result = max(result, cnt)

  for i in range(M):
    cnt = 0
    for j in range(N):
      if matrix[j][i]:
        cnt += 1
        continue
      result = max(result, cnt)
      cnt = 0
    result = max(result, cnt)

  print(f'#{t} {result}')