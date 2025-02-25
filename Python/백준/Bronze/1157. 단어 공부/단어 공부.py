from collections import Counter

word = input().upper()

counter = Counter(word)
max = max(counter.values())

most = [char for char, count in counter.items() if count == max]

if len(most) > 1:
    print('?')
else:
    print(most[0])