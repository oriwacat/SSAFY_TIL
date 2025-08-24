import sys
sys.stdin = open("input.txt")

for t in range(1, 11):
    N = int(input())
    C = list(input())
    box = []
    operator = []
    C.reverse()
    for i in range(N):
        if C[-1].isdigit():
            box.append(C.pop())
        else:
            if not operator:
                operator.append(C.pop())
            elif C[-1] == '*':
                if operator == '*':
                    box.append(C.pop())
                else:
                    operator.append(C.pop())
            elif C[-1] == '+':
                if operator:
                    box.append(operator.pop())
                    if operator:
                        box.append(operator.pop())
                operator.append(C.pop())
    if operator:
        box.append(operator.pop())
        if operator:
            box.append(operator.pop())


    print(*box)
