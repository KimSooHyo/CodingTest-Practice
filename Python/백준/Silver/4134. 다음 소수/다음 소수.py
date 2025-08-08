import sys
import math
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(math.isqrt(num))
    for i in range(3, limit+1, 2):
        if num % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    while not is_prime(n):
        n += 1
    print(n)