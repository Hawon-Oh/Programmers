def solution(survey, choices):
    answer = ''
    # survey와 choices를 for문
    # choice 점수 - 4하고 양수이면 survey 앞에꺼에 더하고
    # 음수이면 +로 바꾼 후 뒤에꺼에 더함
    # for문 끝나면 더 큰걸 answer에 더하고 같으면 사전 앞의 알파벳 더함
    
    survey_dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
                  'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for su, ch in zip(survey, choices):
        ch -= 4
        if ch > 0:
            survey_dic[su[1]] += ch
        elif ch < 0:
            survey_dic[su[0]] += ch * -1
    
    if survey_dic['R'] >= survey_dic['T']:
        answer += 'R'
    elif survey_dic['R'] < survey_dic['T']:
        answer += 'T'
        
    if survey_dic['C'] >= survey_dic['F']:
        answer += 'C'
    elif survey_dic['C'] < survey_dic['F']:
        answer += 'F'
        
    if survey_dic['J'] >= survey_dic['M']:
        answer += 'J'
    elif survey_dic['J'] < survey_dic['M']:
        answer += 'M'
        
    if survey_dic['A'] >= survey_dic['N']:
        answer += 'A'
    elif survey_dic['A'] < survey_dic['N']:
        answer += 'N'
    
    print(survey_dic)
    
    return answer










