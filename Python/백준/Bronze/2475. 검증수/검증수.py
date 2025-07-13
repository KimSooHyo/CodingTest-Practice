sum_n = 0

n_list = list(map(int,input().split()))
for n in n_list:
    sum_n += n**2
    
print(sum_n%10)