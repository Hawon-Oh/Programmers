def solution(lottos, win_nums):
    # 최저개수 = 6 - 안겹친 로또정답 숫자개수
    # 최대개수 = 최저개수 + 0의 개수
    
    min_match = 6 - len(set(win_nums) - set(lottos))
    max_match = min_match + lottos.count(0)
    
    # matching nums to ranking
    low_rank = 7 - min_match
    high_rank = 7 - max_match
    
    # bottom thredhold is rank 6, so 7 -> 6
    if low_rank > 5: low_rank = 6
    if high_rank > 5: high_rank = 6
    
    return [high_rank, low_rank]