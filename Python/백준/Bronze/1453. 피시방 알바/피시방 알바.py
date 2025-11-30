n = int(input())

pc = [0] * 101
cus = list(map(int, input().split()))
ans = 0

for c in cus:
    if pc[c] != 0:
        ans += 1
    else:
        pc[c] = 1

print(ans)