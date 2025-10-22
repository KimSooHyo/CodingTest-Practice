N = int(input())
M = int(input())
material = list(map(int, input().split()))
cnt = 0
i=0
while i < len(material):
    m = material[i]
    # print(m)
    if M - m in material[i+1:]:
        material.remove(m)
        material.remove(M-m)
        cnt += 1
        # print(material)
    else:
        i += 1
        
print(cnt)