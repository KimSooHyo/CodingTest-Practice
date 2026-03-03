while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    rem = 0
    length = 0
    
    while True:
        rem = (rem * 10 + 1) % n
        length += 1
        if rem == 0:
            print(length)
            break