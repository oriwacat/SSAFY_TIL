import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input().strip())
alien_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
our_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dit = {a:b for a,b in zip(alien_number, our_number)}

for _ in range(T):
  N, M = input().split()
  number = list(map(str, input().split()))
  trans = []
  result = []
  for x in number:
    trans.append(dit[x])
  
  trans.sort()

  for y in trans:
    result.append(alien_number[y])

  print(N)
  print(' '.join(result))
