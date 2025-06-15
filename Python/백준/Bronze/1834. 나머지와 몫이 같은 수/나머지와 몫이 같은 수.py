"""
x / n = q
x % n = r
q = r

x = n * q + r
x = n * q + q = q(n+1)
"""

n = int(input())
total = 0

for q in range(1, n):
    total += q*(n+1)
    
print(total)