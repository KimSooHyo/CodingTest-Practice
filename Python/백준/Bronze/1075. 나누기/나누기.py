n = int(input())
f = int(input())

n = n//100*100
while(1):
    if n % f == 0:
        print(str(n)[-2:])
        break
    
    n += 1