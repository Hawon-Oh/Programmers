def solution(price, money, count):
    # 1 2 3 4 5
    answer = money - (sum([_ for _ in range(1, count + 1)]) * price)
    if answer > 0:
        return 0

    return answer * -1