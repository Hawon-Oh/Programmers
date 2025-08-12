def solution(citations):
    citations.sort()
    # 0 1 1 2 2 2 3 5 6 6
    
    max_h = 0
    
    for i, c in enumerate(citations):
        
        if max_h == c:
            continue
        
        max_h = max(max_h, min(c, len(citations) - i))
    
    return max_h










