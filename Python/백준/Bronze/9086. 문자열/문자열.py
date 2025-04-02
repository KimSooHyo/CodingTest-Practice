import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    str = input()
    print(str[0]+str[-1])