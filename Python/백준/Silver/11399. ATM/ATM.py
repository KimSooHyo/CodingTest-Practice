import sys
input = sys.stdin.readline

N = int(input())
P_list = list(map(int, input().split()))
    
P_list.sort()
total = 0
for i in range(N):
    sliced_list = P_list[:i+1]
    total += sum(sliced_list)
    
print(total)