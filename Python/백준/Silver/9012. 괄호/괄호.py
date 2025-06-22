import sys

def solution(text):
    for t in text:
        if t == '(':
            stack.append(t)
        elif t == ')':
            if not stack:
                return False
            else:
                stack.pop()
    
    if stack:
        return False
    else:
        return True

n = int(sys.stdin.readline().strip())
for _ in range(n):
    stack = []
    
    text = sys.stdin.readline().strip()
    answer = solution(text)
    
    if answer:
        print("YES")
    else:
        print("NO")