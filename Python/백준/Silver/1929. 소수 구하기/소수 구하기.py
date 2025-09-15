import sys
input = sys.stdin.readline

M, N = map(int, input().split())

arr = [i for i in range(N+1)]
arr[0] = arr[1] = 0
end = int(N**(1/2)+1)
for i in range(2, end):
    if arr[i] == 0:
        continue
    for  j in range(i*i, N+1, i):
        arr[j] = 0
        
answer = arr[M:N+1]
for a in answer:
    if a != 0:
        print(a)