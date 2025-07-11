def solution(n, words):
    answer = []
    before_words = []
    for i in range(len(words)):
        
        if i > 0 and (words[i-1][-1] != words[i][0]):
            print(i, words[i], words[i-1][-1], words[i][0])
            return [i%n +1, i//n+1]
        
        if words[i] in before_words:
            print(before_words, print(words[i]))
            return [i%n +1, i//n+1]
        else:
            before_words.append(words[i])
            
    return [0,0]