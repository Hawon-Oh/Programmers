def solution(k, score):
    answer = []
    arr = []
    
    for s in score:
        if len(arr) < k:
            arr.append(s)
        elif arr[0] < s:
            arr[0] = s
            
        arr.sort()
        answer.append(arr[0])
    return answer