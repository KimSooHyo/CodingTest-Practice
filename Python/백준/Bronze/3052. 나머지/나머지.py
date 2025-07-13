import sys
input = sys.stdin.readline
num_set = set()
for _ in range(10):
    n = int(input())
    num_set.add(n%42)
    
print(len(num_set))