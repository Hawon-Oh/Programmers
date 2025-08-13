def solution(info, n, m):
    minimum = n
    memo = set()
    
    def dfs_recur(i, a, b):
        nonlocal minimum
        
        if (i, a, b) in memo or a >= minimum or b >= m or i > len(info):
            return
        
        if i == len(info) and a < minimum:
            minimum = a
            return
        
        memo.add((i, a, b))
        
        dfs_recur(i + 1, a + info[i][0], b)
        dfs_recur(i + 1, a, b + info[i][1])
        
    dfs_recur(0, 0, 0)
    
    return minimum if minimum < n else - 1