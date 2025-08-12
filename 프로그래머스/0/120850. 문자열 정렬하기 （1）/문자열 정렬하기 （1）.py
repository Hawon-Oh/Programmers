def solution(my_string): return sorted([int(d) for d in ''.join(map(lambda x: x if x.isdigit() else '', my_string))])
    