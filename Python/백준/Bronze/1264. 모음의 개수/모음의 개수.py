mo = 'aeiouAEIOU'

while(1):
    cnt = 0
    text = input()
    if text == '#':
        break
    
    for t in text:
        if t in mo:
            cnt += 1
            
    print(cnt)