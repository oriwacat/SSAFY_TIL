# import sys
# sys.stdin = open("GNS_test_input.txt")

T = int(input().strip())
alien_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
our_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# dit = {}
# for i in range(10):
#     dit[alien_number[i]] = our_number[i]

dit = {a:b for a,b in zip(alien_number, our_number)}


print(dit)
# for test_case in range(1, T+1):