def solution(today, terms_orig, privacies):
    answer = []
    t_year, t_month, t_day = map(int, today.split('.'))
    terms = {}
    for t in terms_orig:
        k, v = t.split()
        terms[k] = int(v)
    
    for i, p in enumerate(privacies, start=1):
        date, p_term = p.split()
        
        # 언제 파기돼야 하는지 저장
        # month는 +=이 아닌 =를 씀 (1~12사이 수만 가지니까)
        exp_year, exp_month, exp_day = map(int, date.split('.'))
        exp_year += (exp_month + terms[p_term]) // 12
        exp_month = (exp_month + terms[p_term]) % 12
        
        # 연도와 달 비교
        if exp_year * 12 + exp_month < t_year * 12 + t_month:
            answer.append(i)
            
        # 연도와 달이 같다면 일자를 비교
        elif exp_year * 12 + exp_month == t_year * 12 + t_month:
            if exp_day <= t_day:
                answer.append(i)
        
    return answer



