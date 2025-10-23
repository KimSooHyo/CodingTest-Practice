A, B = map(int, input().split())
N = int(input())
favorite = []
for _ in range(N):
    f = int(input().strip())
    favorite.append(f)
    
distance = [abs(B-A)]
for f in favorite:
    distance.append(abs(B-f)+1)

print(min(distance))
