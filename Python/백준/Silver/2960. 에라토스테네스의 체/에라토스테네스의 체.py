N, K = map(int, input().split())

arr = [True] * (N+1)
arr[0] = False
arr[1] = False

cnt = 0

ans = 0

for i in range(N+1):
    if arr[i] == True:
        for j in range(i, N+1, i):
            if arr[j] == False:
                continue
            arr[j] = False 
            cnt += 1
            
            if cnt == K:
                ans = j
                
print(ans)