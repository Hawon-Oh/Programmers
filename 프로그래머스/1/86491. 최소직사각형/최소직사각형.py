def solution(sizes):
    # 뒤(세로) 길이가 더 길면 swap
    # 앞(가로), 뒤(세로) 각각 가장 큰 max를 저장
    # 두 max 곱해서 리턴
    
    max1, max2 = 0, 0
    
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        
        if max1 < size[0]:
            max1 = size[0]
        if max2 < size[1]:
            max2 = size[1]

    return max1 * max2