def solution(a, b, n):
    # 남은콜라가 a보다 크거나 같을 때까지 while
    # 받은콜라 += (n // a) * b 
    # 남은콜라 = 받은콜라 + (n % a)
    
    left = n
    taken = 0
    
    while left >= a:
        this_time = (left // a) * b
        taken += this_time
        left = this_time + (left % a)
        
    return taken






