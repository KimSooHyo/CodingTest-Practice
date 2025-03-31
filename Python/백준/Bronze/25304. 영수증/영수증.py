import sys

x = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

sum=0

for i in range(n):
    a, b = map(int, input().split())
    sum = sum + a * b
    
if x == sum:
    print("Yes")
else:
    print("No")