"""
만들고자 하는 수열은 "스택에서 pop 되는 순서"

수열이 오름차순이거나

오름차순에서 일부만 뒤바뀐 형태지만,
→ 그 바뀐 순서가 LIFO 구조에 맞는 경우는 가능함.
"""

import sys

n = int(input())
answer = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1 #푸시할 숫자

for a in answer:
    
    #현재 숫자보다 작거나 같을 때까지 푸시
    while current <= a:
        stack.append(current)
        result.append('+')
        current += 1
        
    #top이 num과 같으면 pop
    if stack[-1] == a:
        stack.pop()
        result.append('-')
    else: #만들 수 없는 경우
        print("NO")
        break
else:
    for r in result:
        print(r)