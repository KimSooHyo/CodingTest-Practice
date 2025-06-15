import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    order = sys.stdin.readline().strip()
    
    if order == 'pop':
        if not stack:
            print('-1')
        else:
            print(stack.pop())
            
    elif order == 'size':
        print(len(stack))
        
    elif order == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    elif order == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
    else:
        _, value = order.split()
        stack.append(int(value))
        
    