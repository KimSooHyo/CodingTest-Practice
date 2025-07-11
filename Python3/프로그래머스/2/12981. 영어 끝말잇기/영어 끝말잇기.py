def solution(n, words):

    before_words = []
    before_words.append(words[0])
    
    for i in range(1, len(words)):
        
        if (words[i] in before_words) or (words[i-1][-1] != words[i][0]):
            return [i%n +1, i//n+1]
        else:
            before_words.append(words[i])
            
    return [0,0]