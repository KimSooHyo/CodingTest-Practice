from collections import deque
queue = deque()

N = int(input())
for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    card = queue.popleft()
    queue.append(card)
    
print(queue[0])