n = int(input())

for i in range(n):
    print(' '*i + '*'*(2*(n-i)-1))
    
for i in range(1, n):
    print(' '*(n-i-1)+ '*'*((i*2)+1))