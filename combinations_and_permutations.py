# --- Data ---
items = ['A', 'B', 'C']
r = 2

# --- Generator-based Recursive Functions ---

def permutations(arr, r):
    """ 순열: nPr """
    if r == 0:
        yield ()
        return
    for i, item in enumerate(arr):
        remaining = arr[:i] + arr[i+1:]
        for p in permutations(remaining, r - 1):
            yield (item,) + p

def combinations(arr, r):
    """ 조합: nCr """
    if r == 0:
        yield ()
        return
    if not arr:
        return
    
    first = arr[0]
    remaining = arr[1:]
    
    # first를 포함하는 조합
    for c in combinations(remaining, r - 1):
        yield (first,) + c
    
    # first를 포함하지 않는 조합
    yield from combinations(remaining, r)

def product(arr, r):
    """ 중복 순열: nΠr """
    if r == 0:
        yield ()
        return
    for p in product(arr, r - 1):
        for item in arr:
            yield (item,) + p

def combinations_with_replacement(arr, r):
    """ 중복 조합: nHr """
    if r == 0:
        yield ()
        return
    if not arr:
        return

    first = arr[0]
    
    # first를 포함하는 조합 (중복 허용)
    for c in combinations_with_replacement(arr, r - 1):
        yield (first,) + c
        
    # first를 포함하지 않고 다음 원소들로만 조합 생성
    yield from combinations_with_replacement(arr[1:], r)


# --- Execution ---

print(f"순열 ({len(items)}P{r}):")
print(list(permutations(items, r)))
print("-" * 20)

print(f"조합 ({len(items)}C{r}):")
print(list(combinations(items, r)))
print("-" * 20)

print(f"중복 순열 ({len(items)}Π{r}):")
print(list(product(items, r)))
print("-" * 20)

print(f"중복 조합 ({len(items)}H{r}):")
print(list(combinations_with_replacement(items, r)))
print("-" * 20)


# --- 사용자 추가 코드 및 설명 ---
#
# 아래 코드는 n개의 원소를 가지는 배열 arr의 각 자리에 0부터 m-1까지의 숫자를
# 채워 넣는 모든 경우의 수를 출력합니다.
# 이는 m개의 아이템으로 만들 수 있는 길이 n의 중복 순열을 생성하는 것과 같습니다.
#
# - recur(depth): depth는 현재 채워야 할 배열의 인덱스(위치)를 의미합니다.
# - 종료 조건 (depth == n): depth가 배열의 길이 n과 같아지면, 배열이 하나의
#   순열로 완성되었음을 의미하므로 출력합니다.
# - 재귀 호출: for 루프를 통해 현재 depth 위치에 0부터 m-1까지의 숫자를
#   각각 대입해본 후, 다음 위치를 채우기 위해 recur(depth + 1)를 호출합니다.

def recur(depth):
    if depth == n:
        print(*arr)
        return

    for i in range(m):
        arr[depth] = i
        recur(depth + 1)

print("사용자 추가 코드 실행 결과 (3Π3 중복 순열):")
n = 3
m = 3
arr = [0 for i in range(n)]
recur(0)

# --- 사용자 추가 코드 (순열) 보강 ---
#
# 순열을 구현하신 recuu 코드의 구조를 유지하면서, 범용적으로 동작하도록 보강했습니다.
# 1. k, n을 r과 items 길이에 연결했습니다.
# 2. 방문 여부를 확인하는 visited 배열을 초기화하는 코드를 추가했습니다.
# 3. 숫자(i) 대신 실제 데이터(items[i])가 배열에 담기도록 수정했습니다.
# 4. 완성된 순열을 출력하는 코드를 추가했습니다.
def recuu(depth):
    # depth가 뽑을 개수 k(r)에 도달하면, 완성된 순열 arr를 출력
    if depth == k:
        print(*arr)
        return

    # n(items의 길이)만큼 순회
    for i in range(n):
        # i번째 아이템을 이미 사용했다면 건너뛰기
        if visited[i]:
            continue

        # arr의 현재 depth 위치에 i번째 아이템을 할당
        arr[depth] = items[i]
        # i번째 아이템을 사용했다고 표시
        visited[i] = True
        # 다음 depth를 채우기 위해 재귀 호출
        recuu(depth + 1)
        # 재귀 호출이 끝났으면, i번째 아이템을 다른 순열에서 사용할 수 있도록 미사용 처리
        visited[i] = False

print("\n" + "-" * 20)
print("사용자 추가 코드(순열) 보강 후 실행 결과:")
# k: 뽑을 개수 (r), n: 전체 아이템 개수
k = r
n = len(items)
# r (뽑을 개수) 만큼의 공간을 가진 배열 생성
arr = [None] * k
# 방문 여부를 기록하는 배열 생성
visited = [False] * n
# 재귀 함수 시작
recuu(0)

# --- 사용자 추가 코드 (조합) 보강 ---
#
# 조합을 구현하신 aa 코드의 구조를 유지하면서, 범용적으로 동작하도록 보강했습니다.
# 1. k, n을 r과 items 길이에 연결하고, arr 배열을 초기화했습니다.
# 2. 숫자(i) 대신 실제 데이터(items[i])가 배열에 담기도록 수정했습니다.
# 3. 완성된 조합을 출력하는 코드를 추가했습니다.
# 4. 재귀의 시작 인덱스를 1이 아닌 0으로 수정하여 모든 원소가 조합에 포함될 수 있도록 했습니다.
def aa(depth, start):
    # depth가 뽑을 개수 k(r)에 도달하면, 완성된 조합 arr를 출력
    if depth == k:
        print(*arr)
        return

    # start 인덱스부터 n(items의 길이)까지 순회
    for i in range(start, n):
        # arr의 현재 depth 위치에 i번째 아이템을 할당
        arr[depth] = items[i]
        # 다음 depth를 채우고, 다음번엔 현재 선택한 아이템 다음부터(i+1) 탐색하도록 재귀 호출
        aa(depth + 1, i + 1)

print("\n" + "-" * 20)
print("사용자 추가 코드(조합) 보강 후 실행 결과:")
# k: 뽑을 개수 (r), n: 전체 아이템 개수
k = r
n = len(items)
# r (뽑을 개수) 만큼의 공간을 가진 배열 생성
arr = [None] * k
# 재귀 함수 시작 (start는 0부터)
aa(0, 0)



# --- 사용자 추가 코드 (중복 조합) 보강 ---
#
# 마지막으로 중복 조합을 구현하는 코드입니다.
# 조합을 구현한 aa 함수와 거의 동일하지만, 재귀 호출 시 i + 1 대신 i를 넘겨줍니다.
# 이 작은 차이가 현재 선택한 아이템을 다음 탐색에서도 다시 선택할 수 있게 하여 '중복'을 허용합니다.

def bb(depth, start):
    # depth가 뽑을 개수 k(r)에 도달하면, 완성된 중복 조합 arr를 출력
    if depth == k:
        print(*arr)
        return

    # start 인덱스부터 n(items의 길이)까지 순회
    for i in range(start, n):
        # arr의 현재 depth 위치에 i번째 아이템을 할당
        arr[depth] = items[i]
        # 다음 depth를 채우고, 다음번에도 현재 선택한 아이템부터(i) 탐색하도록 재귀 호출
        bb(depth + 1, i)

print("\n" + "-" * 20)
print("사용자 추가 코드(중복 조합) 보강 후 실행 결과:")
# k: 뽑을 개수 (r), n: 전체 아이템 개수
k = r
n = len(items)
# r (뽑을 개수) 만큼의 공간을 가진 배열 생성
arr = [None] * k
# 재귀 함수 시작 (start는 0부터)
bb(0, 0)