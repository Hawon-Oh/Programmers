def solution(schedules, timelogs, startday):
    answer = 0
    
    for n in range(len(schedules)):
        hope_time_min = (schedules[n] // 100) * 60 + (schedules[n] % 100)
        day = startday      # startday부터 7일 카운터 (주말은 6, 7)
        
        for time_min in ((tl // 100) * 60 + (tl % 100) for tl in timelogs[n]):       
            # 한번이라도 주말 아닐 때 10분초과 지각 시 break
            if day not in [6, 7, 13] and hope_time_min + 10 < time_min:
                break
                
            day += 1
        
        # 7일 동안 지각없었으면 합격인원 1추가
        if startday + 7 == day: answer += 1
            
    return answer