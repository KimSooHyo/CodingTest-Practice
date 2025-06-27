def solution(bandage, health, attacks):
    cnt = 0
    j = 0
    max_health = health
    for i in range(attacks[0][0], attacks[-1][0]+1):
        
        print(i, j, health)
        
        if attacks[j][0] == i:
            health -= attacks[j][1]
            cnt = 0
            j += 1
        else:
            health += bandage[1]
            cnt += 1
            if cnt == bandage[0]:
                health += bandage[2]
                cnt = 0
            
        if health > max_health:
            health = max_health
            
        if health <= 0:
            return -1
    return health

