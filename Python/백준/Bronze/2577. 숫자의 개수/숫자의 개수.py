import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
m = a*b*c
answer = str(m)

for i in range(10):
    print(answer.count(str(i)))