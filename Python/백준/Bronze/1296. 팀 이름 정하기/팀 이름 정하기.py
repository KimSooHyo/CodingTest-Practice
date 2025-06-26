import sys

name = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

best_score = -1
best_team = ""

for i in range(n):
    team = sys.stdin.readline().strip()
    L = name.count('L') + team.count('L')
    O = name.count('O') + team.count('O')
    V = name.count('V') + team.count('V')
    E = name.count('E') + team.count('E')
    
    score = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    
    if score > best_score or (score == best_score and team < best_team):
        best_team = team
        best_score = score
        
print(best_team)