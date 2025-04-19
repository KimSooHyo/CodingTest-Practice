sum = int(input())
nine_sum = 0
for i in range(9):
    n = int(input())
    nine_sum += n
    
print(sum - nine_sum)