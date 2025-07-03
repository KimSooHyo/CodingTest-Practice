while True:
    n, m = input().split()
    n, m = int(n), int(m)
    if n == 0 and m == 0:
        break
    elif m % n == 0:
        print("factor")
    elif n % m == 0:
        print("multiple")
    else:
        print("neither")