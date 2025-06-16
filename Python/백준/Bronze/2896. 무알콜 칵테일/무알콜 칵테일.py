a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

x = min(a/i, b/j, c/k)

a_left = a - x*i
b_left = b - x*j
c_left = c - x*k

print(f"{a_left:.4f} {b_left:.4f} {c_left:.4f}")