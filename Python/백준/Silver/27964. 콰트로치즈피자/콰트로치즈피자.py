n = int(input())

words = set(map(str, input().split()))
cnt = 0

for word in words:
    if word.endswith('Cheese'):
        cnt += 1
        
if cnt >= 4:
    print('yummy')
else:
    print('sad')