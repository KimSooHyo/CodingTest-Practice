n = int(input())
integer = int(input())

total = 0
for i in range(n):
    total += (integer%10)
    integer //= 10
    
print(total)