def solution(new_id):
    answer = new_id
    allowed = set("qwertyuiopasdfghjklzxcvbnm1234567890-_.")
    
    # 1. 전부 lowercase로 transfer함
    answer = answer.lower()
    
    # 2. allowed 아닌 char들 전부 제거 (join없으면 문자열 아니라 [a,b,c])
    answer = ''.join([_ for _ in answer if _ in allowed])
    
    # 3. 연속된 '.' 제거
    while ".." in answer:
        answer = answer.replace("..", '.')
    
    # 4. 시작과 끝에 위치한 '.' 제거 (리스트가 empty인지 먼저 체크)
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5. empty면 a
    if not answer:
        answer = "a"
    
    # 6. 길이가 16이상이면 slice. slice 후 마지막 '.'있음 제거
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7. 길이가 2이하이면 3될때까지 마지막 char 반복
    elif len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))
    
    
    return answer