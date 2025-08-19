import sys
sys.stdin = open()

T = int(input())

for t in range(1, T+1):
    # fo_answer = False
    # be_answer = False
    # answer = False
    # cards = list(map(int, input().strip().replace(" ", "")))
    # fo = cards[:3]
    # be = cards[3:]
    # if all(fo[i] + 1 == fo[i+1] for i in range(len(fo)-1)):
    #     fo_answer = True
    # elif fo[0] == fo[1] and fo[1] == fo[2]:
    #     fo_answer = True
    #
    #
    # if all(be[i] + 1 == be[i+ 1] for i in range(len(be) - 1)):
    #     be_answer = True
    # elif be[0] == be[1] and be[1] == be[2]:
    #     be_answer = True
    #
    # answer = fo_answer and be_answer
    #
    # print('true' if answer else 'false')