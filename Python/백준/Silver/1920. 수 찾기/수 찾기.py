import sys

n = int(sys.stdin.readline())
data = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
answer = list(map(int, sys.stdin.readline().split()))

for num in answer:
    print(1 if num in data else 0)