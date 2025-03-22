# 행렬의 크기 N과 M 입력
N, M = map(int, input().split())

# 행렬 A 입력
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 행렬 B 입력
B = []
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 A와 B의 덧셈 결과를 저장할 행렬 C
C = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# 결과 출력
for row in C:
    print(" ".join(map(str, row)))
