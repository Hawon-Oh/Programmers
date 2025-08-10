def solution(arr):
    answer = [arr[0]]
    
    # push할 수가 스택 맨위의 숫자와 같으면 패스
    for n in arr[1:]:
        if answer[-1] == n: continue
        
        answer.append(n)
    
    return answer