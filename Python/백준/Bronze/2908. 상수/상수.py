a, b = input().split()

a_reverse = a[2]+a[1]+a[0]
b_reverse = b[2]+b[1]+b[0]

a_reverse = int(a_reverse)
b_reverse = int(b_reverse)

if a_reverse > b_reverse:
    print(a_reverse)
else:
    print(b_reverse)