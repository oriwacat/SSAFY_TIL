import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    result = 0
    pip = []
    box = list(input())
    for i in range(len(box)):
        if box[] == ')':
            pip.pop()
            result += len(pip)
        pip.append(i)

    # 괄호 열려있는 동안 레이저 지나가면 괄호 개수 를 result에 추가 하기