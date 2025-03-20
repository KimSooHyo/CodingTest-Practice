
n, m = map(int, input().split())
box = [0] * n

for i in range(m):
    a, b, c = map(int, input().split())
    for i in range(a-1, b):
        box[i] = c
        
print(" ".join(map(str, box)))