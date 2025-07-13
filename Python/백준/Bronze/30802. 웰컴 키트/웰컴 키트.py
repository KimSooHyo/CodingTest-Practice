import math
import sys
input = sys.stdin.readline

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

tshirt = 0

for size in sizes:
    tshirt += math.ceil(size/T)
    
print(tshirt)
print(N//P, N%P)