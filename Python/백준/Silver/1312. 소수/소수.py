a, b, n = map(int, input().split())

for _ in range(n):
    a = (a % b) * 10
    digit = a // b

print(digit)