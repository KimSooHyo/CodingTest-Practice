x, y = map(float, input().split())
seven = y/x

n = int(input())
max = y/x
min_price = x
gram = y
for i in range(1, n+1):
    x, y = map(float, input().split())
    price = y/x
    if price > max:
        min = price
        min_price = x
        gram = y
        max = y/x
    
times = 1000/gram
answer = min_price * times
print(f"{answer:.2f}")