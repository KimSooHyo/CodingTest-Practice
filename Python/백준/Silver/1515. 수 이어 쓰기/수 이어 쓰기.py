s = input().strip()
idx = 0
num = 1

while idx < len(s):
    for ch in str(num):
        if idx < len(s) and s[idx] == ch:
            idx += 1
    num += 1

print(num - 1)
