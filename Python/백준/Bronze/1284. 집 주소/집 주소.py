def amho(num):
    #n 은 char
    
    #왼, 오 여백 미리 더하고 시작
    sum = 2
    
    #숫자별 너비 더하기
    for n in num:
        if n == '1':
            sum += 2
        elif n == '0':
            sum += 4
        else:
            sum += 3
    #글자사이 여백        
    sum += (len(num)-1)
    
    return sum

while(1):
    N = input()
    if N == "0":
        break
    
    print(amho(N))
    