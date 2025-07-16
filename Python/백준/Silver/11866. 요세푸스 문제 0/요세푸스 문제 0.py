from collections import deque

n, k = map(int, input().split())

queue = deque(range(1, n+1))  # 1부터 n까지 숫자를 큐에 저장
result = []

while queue:
    queue.rotate(-(k-1))     # k-1번 왼쪽으로 회전 (k번째 사람이 맨 앞으로 오도록)
    result.append(queue.popleft())  # 맨 앞 사람 제거

print(f"<{', '.join(map(str, result))}>")
