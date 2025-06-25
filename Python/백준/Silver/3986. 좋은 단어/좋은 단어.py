import sys

n = int(sys.stdin.readline().strip())
cnt = 0

for i in range(n):
    stack = []
    word = sys.stdin.readline().strip()
    for w in word:
        if not stack or stack[-1] != w:
            stack.append(w)
        else:
            if stack[-1] == w:
                stack.pop()
                
    if not stack:
        cnt += 1
        
print(cnt)