import sys
input = sys.stdin.readline

student = [False] * 31
student[0] = True 

for i in range(28):
    n = int(input())
    student[n] = True
    
for i, s in enumerate(student):
    if s == False:
        print(i)