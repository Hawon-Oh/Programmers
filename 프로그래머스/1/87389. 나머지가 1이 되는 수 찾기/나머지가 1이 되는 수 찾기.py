def solution(n):
    # n을 나눴을 때 나머지가 1이게 하는 가장 작은 수 찾기
    
    smallest = 2
    while smallest < n:
        if n % smallest == 1:
            break
        smallest += 1
    
    return smallest



