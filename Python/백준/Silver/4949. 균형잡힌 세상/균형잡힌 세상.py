import sys

def solution(text):
    stack = []
    
    for t in text:
        if t == '(' or t == '[':
            stack.append(t)
        elif t == ')' or t == ']':
            if not stack:
                return False
            elif stack[-1] == '(' and t == ')':
                stack.pop()
            elif stack[-1] == '[' and t == ']':
                stack.pop()
            else:
                return False
    
    return not stack

while(True):
    text = sys.stdin.readline().rstrip()
    if text == '.':
        break
    
    if solution(text):
        print("yes")
    else:
        print("no")