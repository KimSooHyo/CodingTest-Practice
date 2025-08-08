import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

total_arr = []
total = 0
for a in A:
    total += a
    total_arr.append(total)
    
sorted_arr = sorted(total_arr, reverse=True)[:K]
print(sum(sorted_arr))