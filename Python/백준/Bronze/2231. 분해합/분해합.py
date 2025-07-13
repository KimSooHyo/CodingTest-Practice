n = int(input())

sum_n = 0

for i in range(0, n):
    inumber = i
    sum_n = 0
    while(inumber > 0):
        sum_n += inumber % 10
        inumber //= 10

    if i + sum_n == n:
        break
    
if i + sum_n == n:
    print(i)
else:
    print(0)