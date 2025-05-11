sum = 0
nums = [0] * 10

for i in range(10):
    n = int(input())
    nums[i] = n    

for n in nums:
    sum += n

    if sum >= 100:
        big = sum
        small = sum - n
        break
    else:
        big = sum
        small = sum - n
        
    
big_m = big - 100
small_m = 100 - small

if big_m > small_m:
    print(small)
else:
    print(big)