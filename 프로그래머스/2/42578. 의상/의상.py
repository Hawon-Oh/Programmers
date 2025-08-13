from collections import Counter

def solution(clothes):
    answer = 1
    for n in Counter(c for _, c in clothes).values(): answer *= n + 1
    return answer - 1


