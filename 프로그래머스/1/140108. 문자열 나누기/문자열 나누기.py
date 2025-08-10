def solution(s):
    answer = 0
    
    prev = s[0]
    same = 0
    different = 0
    
    # banana
    for i, cur in enumerate(s):
        if prev == -1:
            prev = cur
            
        if prev == cur:
            same += 1
        else:
            different += 1
        
        if same == different:
            answer += 1
            same, different = 0, 0
            prev = -1
    
    # for문 끝났는데 다르다는건 알파벳 하나남았다는 뜻
    if same != different: answer += 1
            
    return answer