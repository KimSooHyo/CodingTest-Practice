import sys
input = sys.stdin.readline

N = int(input().rstrip())
for i in range(N):
    a, b = map(int, input().rstrip().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")