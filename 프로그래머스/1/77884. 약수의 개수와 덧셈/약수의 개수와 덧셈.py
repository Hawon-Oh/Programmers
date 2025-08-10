def count_divisor(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    
    return count

def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        # 약수 개수가 홀수라면
        if count_divisor(n) % 2 > 0:
            answer -= n
        else:
            answer += n
            
    return answer






