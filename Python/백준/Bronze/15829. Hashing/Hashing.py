alpha = {}
r = 31
m = 1234567891
for i in range(26):
    alpha[chr(ord('a')+i)] = i+1
    
l = int(input())
string = input()

hash_func_sum = 0

for i, s in enumerate(string):
    hash_func_sum += (r ** i) * alpha[s]
    
print(hash_func_sum)