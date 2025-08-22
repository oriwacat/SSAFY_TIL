import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    befo = input()
    after = []
    dicc = {'b':'d','d':'b','p':'q','q':'p'}
    for i in befo[::-1]:
        after.append(dicc[i])
    print(f"#{t} {''.join(after)}")

#박유신
T = int(input())

change_str = {'d': 'b', 'b': 'd', 'q': 'p', 'p': 'q'}

for case in range(1, T + 1):
    string = ''
    for s in input()[::-1]:
        string += change_str[s]
    print(f"#{case} {string}")