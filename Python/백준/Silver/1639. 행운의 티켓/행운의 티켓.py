import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)
result = 0
for l in range(2, n+1, 2):
    for i in range(n - l + 1):
        mid = i+ l // 2
        left = s[i:mid]
        right = s[mid:i+l]
        
        left_sum = sum(int(ch) for ch in left)
        right_sum = sum(int(ch) for ch in right)
        
        if left_sum == right_sum:
            result = max(result, l)
print(result)

# 123231
# 