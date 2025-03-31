import sys

a, b = map(int, input().split())
c = int(sys.stdin.readline().strip())

b = b + c

while(b >= 60):
    a = a + 1
    b = b - 60
    
    if a >= 24:
        a = 0
    
print(a, b)