def solution(people, limit):
    from collections import deque
    
    answer = 0
    people = deque(sorted(people))
    print(people)
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.pop()
    
        answer += 1
        
    if people:
        answer += 1
    
    return answer