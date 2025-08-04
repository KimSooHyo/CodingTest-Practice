import sys
input = sys.stdin.readline

t = int(input())
n = list(map(int, input().split()))
print(min(n) * max(n))