def solution(wallet, bill):
    answer = 0
    
    # 한쪽이라도 지폐가 클 때까지 while 루프
    while max(bill) > max(wallet) or min(bill) > min(wallet):
        bill = [int(max(bill) / 2), min(bill)] # 소수점 버리기
        answer += 1
        
    return answer