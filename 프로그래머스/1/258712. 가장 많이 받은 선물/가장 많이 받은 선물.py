def solution(friends, gifts):
    answer = 0
    
    # 선물받은 횟수. 예시 {'f1': 0, 'f2': 0 ...}
    gift_index = {friend : 0 for friend in friends}
    
    # 다음달 선물 예측치 저장
    gift_predict = {friend : 0 for friend in friends}
    
    # 친구별 선물준 수 dict. 예시 ['f1':{'f1':0, 'f2':0 ...}, 'f2':{'f1':0, 'f2':0}], ...]
    # friends[A][B] == 2 -> 지금까지 A가 B에게 선물 2번 줌
    # ! for문 어디다 집어넣을지 헷갈리지 않게 괄호와 변수를 먼저 쓰고 for은 필요한 괄호 안에 쓰면됨.
    how_many_gifts = {n1: {n2: 0 for n2 in friends} for n1 in friends
}
    
    for gift_log in gifts:
        giver, taker = gift_log.split()
        
        # 선물지수 업데이트
        gift_index[giver] += 1
        gift_index[taker] -= 1
        
        # 두명이서 주고받은 선물기록 업데이트
        how_many_gifts[giver][taker] += 1
        
    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            f1 = friends[i]
            f2 = friends[j]
            
            # 둘이서 주고받은 것 중 f1이 더 줬으면
            # f1이 받을 다음달 선물 추가
            if how_many_gifts[f1][f2] > how_many_gifts[f2][f1]:
                gift_predict[f1] += 1 
            
            # 둘이서 주고받은 것 중 f2가 더 줬으면
            # f2가 받을 다음달 선물 추가
            elif how_many_gifts[f1][f2] < how_many_gifts[f2][f1]:
                gift_predict[f2] += 1
                
            # 둘이서 주고받은 선물주고 받은 적이 없거나 같으면
            # 선물지수가 더 큰 사람이 받음. 이것도 같으면 서로 안받음.
            else:
                if      gift_index[f1] > gift_index[f2]: gift_predict[f1] += 1
                elif    gift_index[f1] < gift_index[f2]: gift_predict[f2] += 1
        
    return max(gift_predict.values())















