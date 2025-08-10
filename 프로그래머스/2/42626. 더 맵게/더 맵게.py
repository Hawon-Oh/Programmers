def solution(scoville, K):
    answer = 0
    import heapq
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        min_sco = heapq.heappop(scoville)
        
        if min_sco >= K: # 모두 K 이상이면
            break
            
        mixed = heapq.heappop(scoville) * 2 + min_sco
        heapq.heappush(scoville, mixed)
        answer += 1
    
    if scoville and scoville[0] >= K:
        return answer
    else:
        return -1