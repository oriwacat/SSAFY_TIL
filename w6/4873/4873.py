import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    A = input()
    stack = []
    for c in A:
        if stack and stack[-1] == c:
            stack.pop()
            continue
        stack.append(c)
    print(f'#{tc} {len(stack)}')
