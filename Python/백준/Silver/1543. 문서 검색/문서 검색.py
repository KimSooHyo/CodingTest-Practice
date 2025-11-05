text = input().strip()
word = input().strip()
length = len(word)
i = 0
cnt = 0

while i + length <= len(text):
    sample = text[i:i+length]
    if sample == word:
        cnt += 1
        i += length
        continue
    i += 1
print(cnt)