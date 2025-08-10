def solution(k, m, score):
    answer = 0
    apples = sorted(score)
    
    for a in apples[len(apples) % m: : m]:
        answer += a * m
    return answer