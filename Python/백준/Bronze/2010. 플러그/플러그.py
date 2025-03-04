import sys
n = int(sys.stdin.readline().rstrip())
sum=0

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    sum += a
    
print(sum-n+1)