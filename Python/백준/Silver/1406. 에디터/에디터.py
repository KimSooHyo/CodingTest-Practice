import sys
input = sys.stdin.readline

left_stack = list(input().strip())
right_stack = []

M = int(input())
for _ in range(M):
    order = input().split()
    if order[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif order[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif order[0] == 'B':
        if left_stack:
            left_stack.pop()
    else:
        left_stack.append(order[1])
        
print("".join(left_stack + list(reversed(right_stack))))