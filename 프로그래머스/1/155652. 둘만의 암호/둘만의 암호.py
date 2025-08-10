def solution(s, skip, index):
    # skip에 포함되는 알파벳은 s에 포함되지 않습니다.
    
    answer = ''
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    # 필요한 알파벳만 선택
    for _ in skip:
        alphabets = alphabets.replace(_, '')
        
    # a b c, a b c, a b c
    # 0 1 2  3 4 5  6 7 8
    # alphabets[index % len(alphabets)]
    
    for ch in s:
        answer += alphabets[(alphabets.find(ch) + index) % len(alphabets)]
    
    return answer