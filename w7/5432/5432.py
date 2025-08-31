import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    result = 0
    pip = []
    box = list(input())
    bl = len(box)
    for i in reversed(range(bl)):
        if box[i] == '(':
            if box[i+1] == ')':
                pip.pop()
                result += len(pip)
                continue
            pip.pop()
            result += 1
            continue
        pip.append(box[i])

    print(f'#{t} {result}')

    # 괄호 열려있는 동안 레이저 지나가면 괄호 개수 를 result에 추가 하기