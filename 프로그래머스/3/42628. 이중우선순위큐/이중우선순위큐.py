def solution(operations):
    import heapq as hq
    min_heap = []
    max_heap = []
    idx = 0
    nonvisited = set()
    
    for op in operations:
        # push
        if op[0] == 'I':
            num = int(op[2:])
            hq.heappush(min_heap, [num, idx])
            hq.heappush(max_heap, [- num, idx])
            nonvisited.add(idx)
            idx += 1
        
        # 최소값 pop
        elif op == "D -1":
            # 이미 visited된 값들은 pop하고, nonvisited인 루트찾기
            while min_heap and min_heap[0][1] not in nonvisited:
                hq.heappop(min_heap)
                
            if min_heap:
                nonvisited.remove(min_heap[0][1])
                hq.heappop(min_heap)
            
        # 최대값 pop
        else:
            # 이미 visited된 값들은 pop하고, nonvisited인 루트찾기
            while max_heap and max_heap[0][1] not in nonvisited:
                hq.heappop(max_heap)
                
            if max_heap:
                nonvisited.remove(max_heap[0][1])
                hq.heappop(max_heap)
    
    if nonvisited:
        while min_heap and min_heap[0][1] not in nonvisited:
            hq.heappop(min_heap)
        while max_heap and max_heap[0][1] not in nonvisited:
            hq.heappop(max_heap)
        
        return [- max_heap[0][0], min_heap[0][0]] 
    else:
        return [0, 0]
    







