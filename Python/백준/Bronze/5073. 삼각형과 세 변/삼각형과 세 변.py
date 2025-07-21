import sys
input = sys.stdin.readline

while True:
    length = list(map(int, input().strip().split()))
    length.sort()
    
    if sum(length) == 0:
        break
    elif length[0] + length[1] <= length[2]:
        print("Invalid")
        continue
    elif length[0] == length[1] == length[2]:
        print("Equilateral")
    elif length[0] != length[1] != length[2]:
        print("Scalene")
    else:
        print("Isosceles")