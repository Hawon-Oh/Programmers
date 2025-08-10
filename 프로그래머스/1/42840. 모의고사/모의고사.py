def solution(answers):
    no_math1 = [1, 2, 3, 4, 5] * 2000
    no_math2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250  # 10000 // 8 = 1250
    no_math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    counter = [0, 0, 0]

    for answer, a1, a2, a3 in zip(answers, no_math1, no_math2, no_math3):
        if answer == a1:
            counter[0] += 1
        if answer == a2:
            counter[1] += 1
        if answer == a3:
            counter[2] += 1

    max_score = max(counter)
    answer = [i + 1 for i, c in enumerate(counter) if c == max_score]
    return answer
