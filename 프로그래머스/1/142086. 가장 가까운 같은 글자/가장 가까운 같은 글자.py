def solution(s):
    answer = []
    dic = {}
    # dic에 있으면 +1, 없으면 -1
    for i, c in enumerate(s):
        # 처음나온 c면 -1 append
        if c not in dic.keys():
            answer.append(-1)
        # 나온 적 있으면 마지막으로 나온거랑 비교 후 append
        else:
            answer.append(i - dic[c])
        
        dic[c] = i # 키의 마지막나온 업뎃
            
    return answer