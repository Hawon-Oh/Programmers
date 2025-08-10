def solution(n, lost, reserve):
    answer = n
    clothes = [1 for _ in range(n)]
    for r in reserve:
        clothes[r - 1] = 2
        
    for l in lost:
        clothes[l - 1] -= 1
        
    for i, c in enumerate(clothes):
        # 현재 옷이 없으면
        if c < 1:
            # 뒷친구 여분옷 체크
            if i > 0 and clothes[i - 1] > 1:
                clothes[i] = 1
                clothes[i - 1] -= 1
            # 앞친구 여분옷 체크
            elif i < n - 1 and clothes [i + 1] > 1:
                clothes[i] = 1
                clothes[i + 1] -= 1
            # 옷 못 빌림
            else:
                answer -= 1
    
    return answer