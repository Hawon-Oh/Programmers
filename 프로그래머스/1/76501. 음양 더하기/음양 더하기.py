def solution(absolutes, signs):
    answer = 0
    # 참이면 +
    for n, is_plus in zip(absolutes, signs):
        if is_plus:
            answer += n
        else:
            answer -= n
    return answer