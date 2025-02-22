num = int(input())

cnt = 0
arr = list(map(int, input().split()))
arr = list(filter(lambda x : x != 1, arr))

for j in arr:
    n = 0
    for i in range(2,j+1):
        if j%i == 0:
            n += 1

    if n == 1:
        cnt += 1
        #print(j , "소수")

print(cnt)