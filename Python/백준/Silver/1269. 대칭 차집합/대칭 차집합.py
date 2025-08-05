import sys
input = sys.stdin.readline

n1, n2 = map(int, input().strip().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a-b) + len(b-a))