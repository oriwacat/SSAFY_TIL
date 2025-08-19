# idx : 뽑으려는 자리
def perm(idx):
    if idx == N:    # 끝까지 뽑았다면
        print(P)
        return
    else:           # 아직 뽑아야 한다면
        # 현재 위치(idx)에 뽑으려는 요소 위치 j가 올 수 있도록 swap
        for j in range(idx, N):     # swap 할 수 있는 범위는 현재 위치의 요소 부터 끝까지
                                    # 현재 위치의 요소도 왜 범위에 들어가야 할까?
                                    # 현재 요소를 선택하는 경우를 고려하기 위함
                                    # 즉, idx 위치에 j 요소를 선택한다는 의미!!
            P[idx], P[j] = P[j], P[idx]     # idx 의 요소가 확정!
            perm(idx+1)
            P[idx], P[j] = P[j], P[idx]     # 선택한 요소를 원래 위치로 복구
                                            # 복구하는 이유는 연산이 꼬이지 않기 위함
                                            # 다음 선택할 요소가 명확한 위치에 있도록 하기 위함

N = 5
P = [i for i in range(1, N+1)]

perm(0)
