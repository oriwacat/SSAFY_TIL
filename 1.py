import sys
sys.stdin = open("sample_input.txt", "r")

def check_brackets(line):
    """주어진 문자열의 괄호 짝이 맞는지 검사하는 함수"""
    stack = []
    # 닫는 괄호를 key, 여는 괄호를 value로 하는 딕셔너리
    bracket_map = {')': '(', '}': '{'}

    for char in line:
        # 여는 괄호는 스택에 추가
        if char in '({':
            stack.append(char)
        # 닫는 괄호일 경우
        elif char in bracket_map:
            # 스택이 비어있으면 짝이 안 맞음 (닫는 괄호가 먼저 나옴)
            if not stack:
                return 0
            # 스택의 마지막 괄호를 꺼냄
            last_open_bracket = stack.pop()
            # 꺼낸 괄호가 짝이 맞지 않으면 실패
            if last_open_bracket != bracket_map[char]:
                return 0

    # 문자열 순회가 끝난 후 스택에 여는 괄호가 남아있으면 실패
    if stack:
        return 0
    
    # 모든 조건을 통과하면 성공
    return 1

T = int(input())
for test_case in range(1, T + 1):
    code_line = input()
    result = check_brackets(code_line)
    print(f"#{test_case} {result}")
