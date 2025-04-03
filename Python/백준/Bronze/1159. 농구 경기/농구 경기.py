import sys

n = int(sys.stdin.readline().strip())

alp = [0] * 26

for _ in range(n):
    name = input()
    char = name[0]
    idx = ord(char) - ord('a')
    alp[idx] += 1

flag = 0    
    
for i in range(26):
    if alp[i] >= 5:
        many_name = ord('a') + i
        print(chr(many_name), end='')
        flag = 1

if flag==0:
    print("PREDAJA")