import sys
sys.stdin = open("input.txt")

T = int(input().strip())
for test_case in range(1, T+1):
  str1 = list(input())
  str2 = list(input())
  result = 0
  for i in range(len(str2)-len(str1)+1):
    if str1 == str2[0+i:len(str1)+i]:
      result = 1
      break
    else:
      pass
    
  print(f'#{test_case} {result}')
      