burger = [0] * 3
drink = [0] * 2

burger[0] = int(input())
burger[1] = int(input())
burger[2] = int(input())

drink[0] = int(input())
drink[1] = int(input())

b_min = min(burger)
d_min = min(drink)

print(b_min+d_min-50)