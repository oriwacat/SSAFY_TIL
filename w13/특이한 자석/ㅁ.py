import sys
sys.stdin = open('sample_input.txt')
from collections import deque

def rotate_magnet(mag, rot, visited):
    if visited[mag] != 0: return

    visited[mag] = rot

    if mag == 0:
        if magnet_list[mag][2] != magnet_list[mag+1][6]:
            rotate_magnet(mag +1, -rot, visited)

    elif mag == 3:
        if magnet_list[mag][6] != magnet_list[mag-1][2]:
            rotate_magnet(mag -1, -rot, visited)

    else:
        if magnet_list[mag][2] != magnet_list[mag+1][6]:
            rotate_magnet(mag +1, -rot, visited)
        if magnet_list[mag][6] != magnet_list[mag-1][2]:
            rotate_magnet(mag -1, -rot, visited)
T = int(input())

for t in range(1, T+1):
    K = int(input())
    n = 4
    magnet_list = [deque(list(map(int,input().split()))) for _ in range(n)]
    rotate_info_list = [list(map(int,input().split())) for _ in range(K)]
    score_sum = 0

    for rotate_info in rotate_info_list:
        magnet_num, rotate_dir = rotate_info

        visited = [0] * n

        rotate_magnet(magnet_num-1, rotate_dir, visited)

        for i, v in enumerate(visited):
            # if v == 1:
            #     pop_data = magnet_list[i].pop()
            #     magnet_list[i].appendleft(pop_data)
            #
            # elif v == -1:
            #     pop_data = magnet_list[i].popleft()
            #     magnet_list[i].append(pop_data)
            #
            magnet_list[i].rotate(v)
    score_list = [1,2,4,8]
    for i in range(4):
        if magnet_list[i][0] == 1:
            score_sum += score_list[i]

    print(f'#{t} {score_sum}')