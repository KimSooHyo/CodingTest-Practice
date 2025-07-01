n = int(input())
stack = []
nums = list(map(int, input().split()))
cnt = 1

for n in nums:
    while stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1
    
    if n == cnt:
        cnt += 1
    else:
        stack.append(n)

while stack and stack[-1] == cnt:
    stack.pop()
    cnt += 1

if not stack:
    print("Nice")
else:
    print("Sad")
        