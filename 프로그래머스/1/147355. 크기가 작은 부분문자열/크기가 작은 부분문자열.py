def solution(t, p):
    answer = 0
    
    # 작거나 작은 부분문자열 찾기
    
    for i in range(len(t) - len(p) + 1):
        # 작거나 같으면 카운트
        if int(t[i:i + len(p)]) <= int(p):
            answer += 1
            
    return answer