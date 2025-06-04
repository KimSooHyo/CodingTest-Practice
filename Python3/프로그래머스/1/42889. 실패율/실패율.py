def solution(N, stages):
    cha =[0] * (N + 2)
    for stage in stages:
        cha[stage] += 1
        
    fails = {}
    total = len(stages)
    
    for i in range(1, N+1):
        if cha[i] == 0:
            fails[i] = 0
        else:
            fails[i] = cha[i]/ total
            total -= cha[i]
    result = sorted(fails, key=lambda x : fails[x], reverse=True)
    return result