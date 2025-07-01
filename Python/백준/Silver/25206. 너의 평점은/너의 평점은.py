grades = {
    'A+' : 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
    'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0,
    'F':0
}
sub = []
total = 0
point = 0

for _ in range(20):
    sub = list(map(str, input().split()))
    p = sub[1]
    g = sub[2]
    
    if g != 'P':
        total += (float(p) * grades[g])
        point += float(p)
        
print(f"{total / point :.6f}")