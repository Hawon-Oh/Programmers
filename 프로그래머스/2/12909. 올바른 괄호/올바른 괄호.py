def solution(s):
    
    # parenthesis open만 스택에 저장
    # close가 나올 때마다 open 스택 pop
    # close가 나왔는데 open 스택이 empty이면 False 리턴
    
    open_stack = []
    
    for o_or_c in s:
        if o_or_c == '(':
            open_stack.append(True)
        else: # ')'일 시
            if open_stack:
                open_stack.pop()
            else:
                return False
    
    # 끝났는데 open_stack이 남았으면 False
    if open_stack:
        return False
    return True