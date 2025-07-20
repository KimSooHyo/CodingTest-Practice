import sys
input = sys.stdin.readline

N = int(input().rstrip())
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    print(a+b)