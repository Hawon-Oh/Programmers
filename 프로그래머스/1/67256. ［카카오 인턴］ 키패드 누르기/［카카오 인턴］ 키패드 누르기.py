def solution(numbers, hand):
    answer = ''
    l_pos = (3, 0)
    r_pos = (3, 2)
    l_able = {1, 4, 7}
    r_able = {3, 6, 9}
    pos_dic = {1:(0, 0), 2:(0, 1), 3:(0, 2),
           4:(1, 0), 5:(1, 1), 6:(1, 2),
           7:(2, 0), 8:(2, 1), 9:(2, 2),
           '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    
    for n in numbers:
        l_dis = abs(l_pos[0] - pos_dic[n][0]) + abs(l_pos[1] - pos_dic[n][1])
        r_dis = abs(r_pos[0] - pos_dic[n][0]) + abs(r_pos[1] - pos_dic[n][1])
        
        if n in l_able:
            answer = answer + 'L'
            l_pos = pos_dic[n]
            
        elif n in r_able:
            answer = answer + 'R'
            r_pos = pos_dic[n]
            
        elif l_dis < r_dis:
            answer = answer + 'L'
            l_pos = pos_dic[n]
            
        elif l_dis > r_dis:
            answer = answer + 'R'
            r_pos = pos_dic[n]
            
        elif hand == "left":
            answer = answer + 'L'
            l_pos = pos_dic[n]
            
        else:
            answer = answer + 'R'
            r_pos = pos_dic[n]
            
    return answer