def solution(numbers):
    answer = set()
    nums = sorted(numbers, reverse=False)
    
    for p, i in enumerate(nums[:-1]):
        for j in nums[p + 1:]:
            answer.add(i + j)
    answer = sorted(list(answer))
    
    return answer