import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

eng = math.ceil(A / C)
math = math.ceil(B / D)

day = eng if eng > math else math

print(L - day)