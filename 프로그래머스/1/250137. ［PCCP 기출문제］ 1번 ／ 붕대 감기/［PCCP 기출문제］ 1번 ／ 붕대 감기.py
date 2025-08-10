def solution(bandage, health, attacks):
    cur_hp = health
    recovery_duration, recovery_per_sec, additional_recovery = bandage
    success_count = attack_count = 0
    
    for t in range(1, max(a[0] for a in attacks) + 1):
        
        # 공격 시
        if attacks[attack_count][0] == t:
            cur_hp -= attacks[attack_count][1]
            success_count = 0
            attack_count += 1
            
            if cur_hp < 1: return -1 # 죽으면 -1 리턴
        
        # 공격 아닐 시
        else:
            success_count += 1
            
            # 초당 + 추가회복
            if success_count == recovery_duration: 
                cur_hp += additional_recovery + recovery_per_sec
                success_count = 0
            # 초당회복
            else:
                cur_hp += recovery_per_sec
                
            if cur_hp > health: cur_hp = health
            
        
    
    return cur_hp