def solution(numbers, target):
    
    def dfs_recur(li, target, cur):
        if not li:
            if cur == target:
                return 1
            return 0
        
        return dfs_recur(li[1:], target, cur + li[0]) + \
               dfs_recur(li[1:], target, cur - li[0])
    
    answer = dfs_recur(numbers, target, 0)
    
    return answer