import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    ch = list(input())
    box = []
    for c in range(len(ch)):
        box.append(ch.pop())
    print(''.join(box))