A, B = map(int, input().split())

low = min(A, B)
high = max(A, B)

count = high - low + 1
total = count * (low + high) // 2

print(total)
