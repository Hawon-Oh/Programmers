def solution(mats, park):
    mats.sort(reverse=True)
    
    is_empty = True
    
    # 돗자리 큰 것부터 선택
    for ml in mats:
        
        # park가 8, ml이 3이면 5
        
        # 체크할 row, col 선택
        for col in range(len(park[0]) - ml + 1):
            for row in range(len(park) - ml + 1):
                is_empty = True # 플래그
                
                # 선택된 [row, col] 좌표에 돗자리 들어가나 체크
                for i in range(ml):
                    for j in range(ml):
                        if park[row + i][col + j] != '-1':
                            is_empty = False
                
                if is_empty == True:
                    return ml
                
    return -1