from collections import deque

def solution(people, limit):
    cnt = 0
    queue = deque(sorted(people, reverse = True))
    print(queue)
    
    while queue:
        if queue[0] + queue[-1] <= limit and len(queue) >= 2:
            cnt += 1
            queue.popleft()
            queue.pop()
        else:
            queue.popleft()
            cnt += 1
    
    return cnt