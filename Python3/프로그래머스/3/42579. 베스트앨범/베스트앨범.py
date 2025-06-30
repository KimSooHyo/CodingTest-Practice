def solution(genres, plays):
    answer = []
    
    genres_dict = {}
    plays_dict = {}
    
    for i in range(len(plays)):
        g = genres[i]    
        p = plays[i]
        if g not in genres_dict:
            genres_dict[g] = []
            plays_dict[g] = 0
        
        genres_dict[g].append((i, p))
        plays_dict[g] += p
        
    sorted_genres = sorted(plays_dict.items(), key = lambda x : x[1], reverse=True)
    
    for genre, _ in sorted_genres:
        sorted_songs = sorted(genres_dict[genre], key = lambda x : (-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])
        
    return answer