n = input()

answer = 0
for c in n:
    answer = (answer * 10 + int(c)) % 20000303
    
print(answer)