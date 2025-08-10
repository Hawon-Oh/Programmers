def solution(cards1, cards2, goal):
    
    # goal에서 한단어씩 꺼내옴. cards1과 cards2 next에 있으면
    # 해당카드 인덱스 1증가
    # 해당단어가 없으면 No 리턴
    # for문 무사히 끝났으면 Yes 리턴
    
    # 카드는 다른 원소만 포함함
    
    card_i1 = 0
    card_i2 = 0
    for word in goal:
        flag = False
        if card_i1 < len(cards1):
            if cards1[card_i1] == word:
                card_i1 += 1
                flag = True
                
        if card_i2 < len(cards2):    
            if cards2[card_i2] == word:
                card_i2 += 1
                flag = True
                
        if flag == False:
            return "No"
    
    return "Yes"

