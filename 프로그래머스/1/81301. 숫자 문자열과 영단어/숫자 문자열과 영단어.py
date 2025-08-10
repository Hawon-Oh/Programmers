def solution(s):
    num_dic = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', 
               "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    
    for k in num_dic:
        s = s.replace(k, num_dic[k])
    
    return int(s)