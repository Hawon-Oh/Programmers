def solution(players, m, k):
    from math import ceil
    
    server_added = 0
    server = [0 for _ in range(24)]
    
    # 시간당 증설된 서버개수 저장하는 배열
    # 정적 플레이어수는 서버수 * m 이상 ~ (서버수 + 1) * m미만
    # 한번 증설되면 +k인덱스만큼 배열 +1
    # 총 몇번의 서버증설이 있었나 리턴
    
    for i, p in enumerate(players):
        # 수용가능 인원
        server_capa = (server[i] + 1) * m - 1
        
        
        # 플레이어 수가 수용가능 초과 시
        if p > server_capa:
            # 서버 얼마나 증설해야 하나 계산
            server_needed = ceil((p - server_capa) / m)
            server_added += server_needed
            
            # k시간만큼 서버증설
            for j in range(k):
                if i + j > 23: break
                
                server[i + j] += server_needed
        
        print(server[i])
        
    return server_added











