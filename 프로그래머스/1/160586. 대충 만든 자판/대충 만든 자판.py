def solution(keymap, targets):
    answer = []
    
    # 키들을 set과 dict으로 변환
    # 없는 알파벳있으면 return -1
    # for문 끝나면 합계를 저장 후 다음 타겟으로 첨부터 반복
    
    # set과 dict 생성
    all_keys = set(k for km in keymap for k in km)
    key_dic = {k : 999999 for k in all_keys}
    for km in keymap:
        for i, k in enumerate(km):
            if key_dic[k] > i + 1:
                key_dic[k] = i + 1
    
    for t in targets:
        if all(ch in all_keys for ch in t) != True:
            answer.append(-1)
            continue
        
        answer.append(sum([key_dic[ch] for ch in t]))
    
    return answer