# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

N = int(input())
length = 0
digit = 1
start = 1

while start * 10 <= N:
    length += (start * 10 - start) * digit
    digit += 1
    start *= 10
    
length += (N- start+1) * digit
print(length)