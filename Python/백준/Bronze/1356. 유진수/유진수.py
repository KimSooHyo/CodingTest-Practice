def is_yujinsu(n):
    num_str = str(n)
    length = len(num_str)
    
    for i in range(1, length):
        left = num_str[:i]
        right = num_str[i:]
        
        # 각 부분의 자리수 곱 계산
        left_product = 1
        for ch in left:
            left_product *= int(ch)
        
        right_product = 1
        for ch in right:
            right_product *= int(ch)
        
        if left_product == right_product:
            return "YES"
    
    return "NO"

# 입력
n = input().strip()
print(is_yujinsu(n))
