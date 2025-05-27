n = int(input())
files = [input() for _ in range(n)]
pat = list(files[0])

for i in range(1, n):
    for j in range(len(pat)):
        if pat[j] != files[i][j]:
            pat[j] = '?'
    
print(''.join(pat))