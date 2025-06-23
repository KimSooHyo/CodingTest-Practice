#스택 문제인데 스택 없이 풀었음

t = input()

stick_cnt = 0
total = 0
for i in range(len(t)):
    if t[i] == '(' and t[i+1] == ')':
        total += stick_cnt
        i += 1
    elif t[i] == '(' and t[i+1] != ')':
        stick_cnt += 1
    elif t[i] == ')' and t[i-1] != '(':
        stick_cnt -= 1
        total += 1
        
print(total)