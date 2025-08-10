def solution(name):
    updown = sum(map(lambda c: min(ord(c) - ord('A'), ord('Z') - ord(c) + 1), name))
    not_a = set([i for i, _ in enumerate(name) if _ != 'A'])  
    
    def bfs_recur(loc, count, length, i):
        if i == -1:
            i = length - 1
        elif i == length:
            i = 0
        loc = loc.copy()
        loc.discard(i)
        
        if not loc or count == length - 1:
            return count
        
        count += 1    
        left = bfs_recur(loc, count, length, i - 1)
        right = bfs_recur(loc, count, length, i + 1)
        
        return min(left, right)
        
    return updown + bfs_recur(not_a, 0, len(name), 0)