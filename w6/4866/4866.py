import sys

sys.stdin = open("sample_input.txt")

T = int(input())
C = {'}' : '{', ']' : '[', ')' : '('}
for tc in range(1, T + 1):
    a = input()
    llist = []
    result = 1
    for i in a:
        if i in ['{', '[', '(']:
            llist.append(i)
        if i in ['}', ']', ')']:
            if llist and llist[-1] == C[i]:
                llist.pop()
            else:
                result = 0
    if llist:
        result = 0

    print(f'#{tc} {result}')


















# T = int(input())
#
# for t in range(T):
#     string = input()
#     stack = []
#
#     open_bracket_of = {')': '(', '}': '{', ']': '['}
#
#
#     def check():
#         for char in string:
#             if char in ['(', '{', '[']:
#                 stack.append(char)
#             if char in [')', '}', ']']:
#                 if stack and stack[-1] == open_bracket_of[char]:
#                     stack.pop()
#                 else:
#                     return False
#         if stack:
#             return False
#         return True
#
#
#     print(f"#{t + 1} {int(check())}")