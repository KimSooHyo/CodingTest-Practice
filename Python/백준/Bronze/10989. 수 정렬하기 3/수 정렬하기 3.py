import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
count = [0] * 10001 #1부터 10000까지

for _ in range(N):
    num = int(input())
    count[num] += 1
    
for i in range(1, 10001):
    for _ in range(count[i]):
        print(f"{i}\n")