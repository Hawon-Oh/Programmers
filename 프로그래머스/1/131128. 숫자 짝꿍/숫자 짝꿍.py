def solution(X, Y):
    answer = ""
    # 각 정수 갯수를 센다
    # 정수갯수를 담은 2개의 배열 값이 같은 정수만 배열에 추가
    # 없으면 -1 리턴
    # 9부터 0까지 갯수만큼 string에 더하기
    
    num_x = [0 for n in range(10)]
    num_y = [0 for n in range(10)]
    for n in X:
        num_x[int(n)] += 1
    for n in Y:
        num_y[int(n)] += 1
    
    for i, x, y in zip("9876543210", num_x[-1::-1], num_y[-1::-1]):
        if x > 0 and y > 0:
            answer += i * min(x, y)
    
    # 예외처리
    if answer == '':
        answer = "-1"
        
    if answer[0] == '0':
        answer = "0"
        
    return answer





