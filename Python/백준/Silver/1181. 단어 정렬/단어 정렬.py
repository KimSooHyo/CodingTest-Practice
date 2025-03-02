import sys 

n = int(sys.stdin.readline().strip())
words = set(sys.stdin.readline().strip() for _ in range(n))

sorted_words = sorted(words, key = lambda x : (len(x), x))

print("\n".join(sorted_words))