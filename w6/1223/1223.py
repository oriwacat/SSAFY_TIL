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
                if operator[-1] == '*':
                    box.append(C.pop())
                else:
                    operator.append(C.pop())
            elif C[-1] == '+':
                while operator:
                    box.append(operator.pop())
                operator.append(C.pop())
    while operator:
        box.append(operator.pop())

    result = []
    for i in box:
        if i.isdigit():
            result.append(int(i))
        else:
            a = result.pop()
            b = result.pop()
            if i == '+':
                result.append(a + b)
            elif i == '*':
                result.append(a * b)

    print(f'#{t} {result[0]}')

    

# for t in range(1, 11):
#     N = int(input())
#     C = list(input())
#     box = []
#     operator = []
#     C.reverse()
#     for i in range(N):
#         if C[-1].isdigit():
#             box.append(C.pop())
#         else:
#             if not operator:
#                 operator.append(C.pop())
#             elif C[-1] == '*':
#                 if operator[-1] == '*':
#                     C.pop()
#                     box.append(box.pop() * box.pop())
#                 else:
#                     operator.append(C.pop())
#             elif C[-1] == '+':
#                 if operator[-1] == '*':
#                     operator.pop()
#                     box.append(box.pop() * box.pop())
#                 elif operator[-1] == '+':
#                     operator.pop()
#                     box.append(box.pop() + box.pop())
#                 if operator[-1] == '*':
#                     operator.pop()
#                     box.append(box.pop() * box.pop())
#                 elif operator[-1] == '+':
#                     C.pop()
#                     box.append(box.pop() + box.pop())
#     if operator[-1] == '*':
#         operator.pop()
#         box.append(box.pop() * box.pop())
#     elif operator[-1] == '+':
#         operator.pop()
#         box.append(box.pop() + box.pop())
#     if operator[-1] == '*':
#         operator.pop()
#         box.append(box.pop() * box.pop())
#     elif operator[-1] == '+':
#         C.pop()
#         box.append(box.pop() + box.pop())


#     print(*box)