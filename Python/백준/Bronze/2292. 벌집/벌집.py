n = int(input())
ans = 1
i = 1
while(1):
    ans = ans + i * 6
    if n == 1:
        print(1)
        break
    
    elif n <= ans:
        print(i+1)
        break
    
    
    i += 1 