import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
sorted_x = sorted(set(x))

new_x = {num : i for i, num in enumerate(sorted_x)}
print(' '.join(str(new_x[num]) for num in x))