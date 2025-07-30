import sys
input = sys.stdin.readline

stack = []
sentence = input().strip()
bomb = input().strip()

for s in sentence:
    stack.append(s)
    
    if "".join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]
        
print("".join(map(str, stack)) if stack else "FRULA")