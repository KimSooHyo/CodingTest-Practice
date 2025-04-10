def solution(answers):
    
    supos = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    scores = [0] * 3
    
    for i, answer in enumerate(answers):
        for j, supo in enumerate(supos):
            if answer == supo[i % len(supo)]:
                scores[j] += 1
                
    max_score = max(scores)
    highest = []
    for i, score in enumerate(scores):
        if score == max_score:
            highest.append(i+1)
    
    return highest