n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sorted = sorted(A, reverse=True)
B_sorted = sorted(B)

total = 0
for a, b in zip(A_sorted, B_sorted):
    total += a * b
    
print(total)