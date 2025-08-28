import sys
input = sys.stdin.readline

N = int(input())
numbers = [input().strip() for _ in range(N)]
numbers_int = []
for n in numbers:
    cnt = 0
    for c in n:
        if c.isdigit():
            cnt += int(c)
    numbers_int.append([n, cnt])

sorted_numbers = sorted(numbers_int, key=lambda x : (len(x[0]), x[1], x))

for nums in sorted_numbers:
    print(nums[0])