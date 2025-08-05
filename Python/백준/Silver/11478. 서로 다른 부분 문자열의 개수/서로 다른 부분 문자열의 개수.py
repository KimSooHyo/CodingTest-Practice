s = input()
words = set()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        words.add(s[i:j])
    
print(len(words))