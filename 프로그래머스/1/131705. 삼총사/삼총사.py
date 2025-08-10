def solution(number):
    answer = 0
    c = 0
    for i1, n1 in enumerate(number[:-2]):
        for i2, n2 in enumerate(number[i1 + 1:-1]):
            for n3 in number[i1 + i2 + 2:]:
                c += 1
                if sum([n1, n2, n3]) == 0:
                    answer += 1
    print(c)
    return answer