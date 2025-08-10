def solution(progresses, speeds):
    from collections import deque
    
    answer = []
    prog_dq = deque(progresses)
    sp_dq = deque(speeds)
    cur_d = 0
    
    while prog_dq:
        cur_d += 1
        pop_count = 0
        
        while prog_dq and cur_d * sp_dq[0] + prog_dq[0] > 99:
            prog_dq.popleft()
            sp_dq.popleft()
            pop_count += 1
        else:
            if pop_count > 0:
                answer.append(pop_count)
        
    return answer






