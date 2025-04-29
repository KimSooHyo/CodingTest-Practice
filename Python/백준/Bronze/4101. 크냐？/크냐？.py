def bigger(a, b):
    if a > b:
        print("Yes")
        return
    else:
        print("No")
        return

while(1):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    bigger(a,b)
    