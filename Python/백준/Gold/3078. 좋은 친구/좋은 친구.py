import sys
input = sys.stdin.readline

N, K = map(int, input().split())
friends = [input().strip() for _ in range(N)]
arr = [len(friend) for friend in friends]
len_name = [0] * 21

cnt = 0
for i in range(N):
    if K < i:
        len_name[arr[i-K-1]] -= 1
        
    cnt += len_name[arr[i]]
    len_name[arr[i]] += 1
    
print(cnt)