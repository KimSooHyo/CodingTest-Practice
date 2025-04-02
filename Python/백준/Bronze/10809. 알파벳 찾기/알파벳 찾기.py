S = input().strip()

list = [-1] * 26

for idx, char in enumerate(S):
    char_idx = ord(char) - ord('a')
    if list[char_idx] == -1:
        list[char_idx] = idx
        
print(' '.join(map(str, list)))