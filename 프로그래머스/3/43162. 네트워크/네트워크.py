def solution(n, computers):
    answer = 0
    visited = [False] * len(computers)
    
    def dfs(node):
        visited[node] = True
        for n, c in enumerate(computers[node]):
            if not visited[n] and c:
                dfs(n)
                
        
    for node in range(len(computers)):
        if not visited[node]:
            answer += 1
            dfs(node)
        
    return answer







