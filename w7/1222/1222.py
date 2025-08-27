import sys
sys.stdin = open('input.txt')
from collections import deque

T = 10
for t in range(1, T+1):
    N = int(input().strip())
    calcul = deque(input().strip())
    box = []
    operator = []
    for i in range(N):
        if calcul[0].isdigit():
            box.append(calcul.popleft())
        else:
            if operator:
                a = box.pop()
                b = box.pop()
                calcul.popleft()
                box.append(int(a) + int(b))
            else:
                operator.append(calcul.popleft())
    a = box.pop()
    b = box.pop()
    operator.pop()
    box.append(int(a) + int(b))
    print(f'#{t} {box[0]}')