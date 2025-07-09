n, b = map(int, input().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ''
while n > 0:
    n, rem = divmod(n, b)
    result = digits[rem] + result

print(result)