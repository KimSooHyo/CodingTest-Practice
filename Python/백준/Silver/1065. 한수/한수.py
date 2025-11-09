def is_hansu(x):
    s = list(map(int, str(x)))
    if len(s) <= 2:
        return True
    return (s[1] - s[0]) == (s[2] - s[1])
n = int(input())
count = 0

for i in range(1, n + 1):
    if is_hansu(i):
        count += 1

print(count)
