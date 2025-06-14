def solution(s):
    stack = []
    
    for c in s:
        if not stack:
            stack.append(c)
        elif c != stack[-1]:
            stack.append(c)
        elif c == stack[-1]:
            stack.pop()
    
    if not stack:
        return 1
    else:
        return 0