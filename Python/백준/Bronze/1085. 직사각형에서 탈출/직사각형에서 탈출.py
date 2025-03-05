n = list(map(int, input().split()))

num = [0] * 4

num[0] = abs(0-n[0])
num[1] = abs(n[2]-n[0])

num[2] = abs(0-n[1])
num[3] = abs(n[3]-n[1])

print(min(num))