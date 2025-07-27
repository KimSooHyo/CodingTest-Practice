import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
layers = min(N, M) // 2  # 테두리 개수

for layer in range(layers):
    elements = []

    # 테두리 좌표 저장
    # 위쪽
    for i in range(layer, M - layer):
        elements.append(A[layer][i])
    # 오른쪽
    for i in range(layer + 1, N - 1 - layer):
        elements.append(A[i][M - 1 - layer])
    # 아래쪽
    for i in range(M - 1 - layer, layer - 1, -1):
        elements.append(A[N - 1 - layer][i])
    # 왼쪽
    for i in range(N - 2 - layer, layer, -1):
        elements.append(A[i][layer])

    # 회전
    r = R % len(elements)
    elements = elements[r:] + elements[:r]

    # 다시 집어넣기
    idx = 0
    for i in range(layer, M - layer):
        A[layer][i] = elements[idx]
        idx += 1
    for i in range(layer + 1, N - 1 - layer):
        A[i][M - 1 - layer] = elements[idx]
        idx += 1
    for i in range(M - 1 - layer, layer - 1, -1):
        A[N - 1 - layer][i] = elements[idx]
        idx += 1
    for i in range(N - 2 - layer, layer, -1):
        A[i][layer] = elements[idx]
        idx += 1

# 결과 출력
for row in A:
    print(*row)