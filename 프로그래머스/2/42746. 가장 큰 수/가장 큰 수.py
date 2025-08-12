def solution(numbers):
    answer = ''
    numbers = [str(n) for n in numbers]
    """
    # 속도느려서 버블정렬 불가능
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):
            # 순서 바꾼게 더 크면 서로 순서 바꿈
            if numbers[j] + numbers[j + 1] < numbers[j + 1] + numbers[j]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    """
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = "".join(numbers)
    
    if answer[0] == '0':
        answer = "0"
        
    return answer