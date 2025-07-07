import sys
import math

t = int(sys.stdin.readline().strip())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(math.comb(m, n))