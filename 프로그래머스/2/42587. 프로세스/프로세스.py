def solution(priorities, location):
    from collections import deque
    
    task_dq = deque((i, p) for i, p in enumerate(priorities))
    pri_dq = sorted(priorities, reverse=True)
    
    # 0부터 priorities 길이까지 중요도와 index를 deque에 저장
    # priorities를 sort해서 저장
    # 왼쪽씩 pop하며 해당 것의 우선순위가 가장 높으면 실행 +1,
    # 아니면 다시 push(오른쪽)
    # 실행된 숫자가 location과 같으면 몇번째 실행인지 리턴
    
    execute_count = 0
    
    while task_dq:
        cur = task_dq.popleft()
        
        if cur[1] == pri_dq[execute_count]:
            execute_count += 1
            
            # print(cur[0], cur[1])
            
            if cur[0] == location:
                 return execute_count
            
        else:
            task_dq.append(cur)
    
    return execute_count






