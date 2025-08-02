def solution(genres, plays):
    answer = []
    dict = {}
    for v, g in enumerate(genres):
        if g not in dict:
            dict[g] = plays[v]
        else:
            dict[g] += plays[v]
    print(dict)
    
    genre = set(genres)
    print(genre)
    genre_play = []
    for i in range(len(genres)):
        genre_play.append([genres[i], plays[i], dict[genres[i]], i])
    print(genre_play)
    
    
    sorted_list = sorted(genre_play, key=lambda x: ((-x[2]), -x[1], x[3]))
    
    g = []

    for i in range(len(sorted_list)):
        print("i:", i)
        print("answer", answer)
        print(len(answer), (len(genre) * 2))
        print("g : ",g)
        if len(answer) >= (len(genre) * 2):
            print(len(answer), (len(genre) * 2))
            return answer
        
        print("g count : ",g.count(sorted_list[i][0]))
        if g.count(sorted_list[i][0]) >= 2:
            continue
        print("append suc")
        answer.append(sorted_list[i][3])
        g.append(sorted_list[i][0])
    
    return answer