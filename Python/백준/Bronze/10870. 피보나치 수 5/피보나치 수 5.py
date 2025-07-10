import sys
sys.setrecursionlimit(1000)
input = sys.stdin.readline

n = int(input())

def recursion(a, b, i):
    if i >= n:
        return a
    return recursion(b, a+b, i+1)
    
print(recursion(0, 1, 0))