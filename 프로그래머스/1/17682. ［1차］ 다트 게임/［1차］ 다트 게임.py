def solution(dartResult):
    answer = 0
    
    was_it_digit = False
    temp = 0
    prev = 0
    for c in dartResult:
        if c.isdigit():
            if was_it_digit:
                temp = temp * 10 + int(c)
            else:
                answer += temp
                prev = temp
                temp = int(c)
                
            was_it_digit = True
            
        else:
            was_it_digit = False
            
            if c == 'D':
                temp **= 2
            
            elif c =='T':
                temp **= 3
            
            elif c == '*':
                temp *= 2
                answer += prev
                
            elif c == '#':
                temp = - temp
    
    answer += temp
    
    return answer