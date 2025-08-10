def solution(N, stages):
    answer = []
    fail_arr = [0 for _ in range(N)]
    
    for i in range(1, N + 1):
        fail = 0
        total = 0
        for j in stages:
            if i == j:
                fail += 1
            if i <= j:
                total += 1
        
        if total == 0:
            fail_rate = 0
        else:
            fail_rate = fail / total
        fail_arr[i - 1] = fail_rate
        
    for _ in range(N):
        max_i = -1
        max_f = -1
        for i, f in enumerate(fail_arr):
            if max_f < f:
                max_i = i
                max_f = f
        
        answer.append(max_i + 1)
        fail_arr[max_i] = -1
    
    return answer