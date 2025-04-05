def digit_sum(n):
    
    
    while(n >= 10):
        sum_x = 0
        for x in str(n):
            sum_x += int(x)
            
        n = sum_x
    
    print(n)

while(1):
    x = int(input())
    if (x == 0):
        break
    digit_sum(x)