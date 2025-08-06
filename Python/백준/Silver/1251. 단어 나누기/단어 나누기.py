import sys
input = sys.stdin.readline

word = input().strip()
n = len(word)
word_list = []
for i in range(1, n-1):
    for j in range(i+1, n):
        a = word[:i]
        b = word[i:j]
        c = word[j:]

        word_list.append(a[::-1]+b[::-1]+c[::-1])
        
# print(sorted(word_list))
print(sorted(word_list)[0])