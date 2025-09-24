K, N = map(int, input().split())

picked = []

def pick(cnt):
    # 종료조건
    if cnt == N:
        print(*picked)
        return

    for i in range(1, K + 1):
        if (
            len(picked) >= 2 and
            picked[-2] == picked[-1] and
            i == picked[-1]
        ):
            continue

        picked.append(i)
        pick(cnt + 1)
        picked.pop()

pick(0)



-------------------------------------


# n: 턴의 수, m: 끝점의 좌표, k: 말의 수, nums: 턴마다 움직일 거리
n, m, k = map(int, input().split())
movings = list(map(int, input().split()))

positions = [1] * (k + 1)
ans = 0

def calc():
    # m에 도달한 말이 몇개인지 센다.
    cnt = 0
    for i in range(1, k + 1):
        if positions[i] >= m:
            cnt += 1
    return cnt

# idx는 moving의 index = 현재 몇 번쨰 움직임을 진행할지
def move(idx):
    global ans

    if idx == n:
        # print(movings)
        ans = max(ans, calc())
        return

    for i in range(1, k + 1):
        if k > 1 and positions[i] >= m:
            continue

        positions[i] += movings[idx] # i를 움직인다.
        move(idx + 1) # 재귀를 한다.
        positions[i] -= movings[idx] # i의 움직임을 돌려놓는다.

move(0)
print(ans)