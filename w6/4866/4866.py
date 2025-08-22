import sys

sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = list(input())
    llist = []
    for i in range(len(N)):
        if N[i] == '(' or N[i] == ')' or N[i] == '{' or N[i] == '}':
            llist.append(N[i])

    while True:
        for i in range(len(llist)//2):
            if llist[i] == llist[i+1]:
                llist.remove(llist[i])
                llist.remove(llist[i+1])
                break

        if len(llist) == 0:
            result = 1
            break

        if len(llist) == 1:
            result = 0
            break
    print(f'#{tc} {result}')

T = int(input())

for t in range(T):
    string = input()
    stack = []

    open_bracket_of = {')': '(', '}': '{', ']': '['}


    def check():
        for char in string:
            if char in ['(', '{', '[']:
                stack.append(char)
            if char in [')', '}', ']']:
                if stack and stack[-1] == open_bracket_of[char]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True


    print(f"#{t + 1} {int(check())}")