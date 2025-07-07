n, m = map(int, input().split())

minus = abs(m - n)
for i in range(n):
    
    if i >= minus:
        if i == minus:
            continue
        else:
            print(minus, i)
    else:
        print(i, i+1)