color = {'black' : 0, 'brown':1, 'red':2, 'orange':3,
         'yellow':4, 'green':5, 'blue':6, 'violet':7,
         'grey':8, 'white':9
         }

c1 = input()
c2 = input()
c3 = input()

ans = 0
ans = color[c1] * 10 + color[c2]
ans = ans * (10 ** color[c3])

print(ans)