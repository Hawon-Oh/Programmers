def solution(name, yearning, photo):
    friendship_calc_arr = []
    friendship_dict = {n : y for n, y in zip(name, yearning)}
    
    for p in photo:
        # dict.get함수는 unexisted key의 디폴트값 지정가능
        friendship_calc_arr.append(sum([friendship_dict.get(n, 0) for n in p]))
        
    return friendship_calc_arr