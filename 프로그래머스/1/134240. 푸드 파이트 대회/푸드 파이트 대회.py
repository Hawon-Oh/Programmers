def solution(food):
    # food원소들을 2로 나눈후 정수로 바꿈.
    # 정수만큼 index를 곱함 (1부터)
    # 0 + reverse로 추가
    
    answer = ''.join(str(i) * int(f / 2) for i, f in enumerate(food[1:], start=1))
    return answer + '0' + answer[-1::-1]