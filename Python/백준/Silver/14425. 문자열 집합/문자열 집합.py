n, m = map(int, input().split())
words = []

for _ in range(n):
    word = input()
    words.append(word)
    
cnt = 0
for _ in range(m):
    answer = input()
    if answer in words:
        cnt += 1
        
print(cnt)