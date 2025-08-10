def solution(babbling):
    # 예로 yayae 가 있으면 aya가 지워지고 ye가 지워짐
    # 이런 경우를 방지하고자 마침표를 집어넣고 나중에 마침표를 지움
    answer = 0
    mamamoo = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        if all(True if m + m not in word else False for m in mamamoo):
            for ma in mamamoo:
                word = word.replace(ma, '.')
            word = word.replace('.', '')
        
            if len(word) == 0:
                answer += 1
            
    return answer