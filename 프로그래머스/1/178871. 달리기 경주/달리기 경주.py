def solution(players, callings):
    p_arr = players[:]
    p_index = {players[i] : i for i in range(len(players))}
    
    for call in callings:
        called_p_i = p_index[call]
        
        # 선수 index dict도 swap
        p_index[call] -= 1
        p_index[p_arr[called_p_i - 1]] += 1
        
        # 선수순위 swap
        p_arr[called_p_i], p_arr[called_p_i - 1] = p_arr[called_p_i - 1], p_arr[called_p_i]
        

    return p_arr