def solution(participant, completion):
    player_dict = {}
    for p in participant:
        if p in player_dict:
            player_dict[p] += 1
        else:
            player_dict[p] = 1
    
    for c in completion:
        if player_dict[c] > 1:
            player_dict[c] -= 1
        else:
            del player_dict[c]
            
    left = list(player_dict.keys())[0]
    return left