total = 0

for _ in range(4):
    x = int(input())
    total += x
    
print(total//60)
print(total % 60)